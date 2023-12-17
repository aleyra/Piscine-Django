from django.urls import path
from chat.views.chatHomeView import ChatHomeView
from chat.views.roomIntoView import RoomIntoView


urlpatterns = [
    path("", ChatHomeView.as_view(), name="chat-home"),
    path('<int:pk>/room/', RoomIntoView.as_view(), name='room-into'),
]