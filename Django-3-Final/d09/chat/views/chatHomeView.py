from django.shortcuts import render
from django.views.generic import ListView
from chat.models import Room


class ChatHomeView(ListView):
    template_name = "chat/chat-home.html"
    model = Room

    def get_queryset(self):
        return Room.objects.filter()


# class ChatHomeView(ListView):
#     def get(self, request):
#         return render(request, 'chat/chat-home.html', {})
