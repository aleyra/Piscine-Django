import json

from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message, Room

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.username = self.scope.get('user').username if self.scope.get('user') else 'user'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_joined',
                'message': 'has joined the chat',
                'sender': self.username,
            }
        )
        self.get_messages()

        # send last 3 messages
        messages = Message.objects.filter(room__label=self.room_name).order_by("-timestamp")[:3]
        for message in reversed(messages):
            self.send(text_data=json.dumps({"message": message.message, "username": message.user.username, "timestamp": message.timestamp.strftime("%H:%M")}))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
        
        #check if room exists
        room = Room.objects.filter(label=self.room_name).first()
        if not room:
            room = Room.objects.create(label=self.room_name)
        Message.objects.create(room=room, user=self.scope["user"], message=message)

    def chat_joined(self, event):
        message = event["sender"] + " " + event["message"]
        self.send(text_data=json.dumps({"message": message}))

    @database_sync_to_async
    def get_messages(self):
        messages = Message.objects.filter(room__label=self.room_name).order_by("-timestamp")[:3]
        for message in reversed(messages):
            async_to_sync(self.send)(text_data=json.dumps({"message": message.message, "username": message.user.username, "timestamp": message.timestamp.strftime("%H:%M")}))