from django.contrib import admin
from .models import Room, Message


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'label',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'content', 'created',)


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)