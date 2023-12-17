from django.http import JsonResponse


def getUsername(request):
    if request.user.is_authenticated:
        user_details = {
            'username': request.user.username,
        }
        return JsonResponse(user_details)
    else:
        return JsonResponse({'error': 'user not log'}, status=401)