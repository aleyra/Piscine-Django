from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse

from django.contrib.auth import authenticate, get_user_model, logout, login

# from account.models import 

# Create your views here.
User = get_user_model()


def home(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            todos = list(User.objects.all().values())
            return JsonResponse({'context': todos})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')