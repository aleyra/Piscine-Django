import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


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
        self.send(text_data=json.dumps({
            'message':  self.username + ' has joined the chat'
        }))

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
            self.room_group_name, 
            {"type": "chat_message",
             "message": message,
             "sender": self.username,
             }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["sender"] + " : " + event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))