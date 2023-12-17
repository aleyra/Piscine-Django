from chat.models import Room
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class RoomIntoView(DetailView):
    model = Room
    template_name = 'chat/chat-room-into.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_label = self.kwargs.get('room_label') 
        context['title'] = 'Room Into'
        context['room_label'] = room_label

        return context
