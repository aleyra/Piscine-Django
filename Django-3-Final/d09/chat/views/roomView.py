from django.shortcuts import render
from django.views import View


class ChatHomeView(View):
    def get(self, request):
        return render(request, 'chat/chat-home.html', {})