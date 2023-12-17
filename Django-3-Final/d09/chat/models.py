from django.db import models
from django.contrib.auth.models import User

# Create models to build a chat using websockets


class Room(models.Model):
    name = models.CharField(max_length=128)
    label = models.SlugField(unique=True, max_length=128)

    def __str__(self):
        return f"Room({self.name})[{self.label}]"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message(from:{self.user.username})(Room:{self.room.name})[content:{self.content}]"
