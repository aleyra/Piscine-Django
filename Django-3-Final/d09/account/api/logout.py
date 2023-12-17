from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout


def logout(request):
    if request.user.is_authenticated:
        data = {
            'message': 'success',
        }
        try:
            auth_logout(request)
            return JsonResponse(data, status=200)
        except Exception as e:
            print("logout error : ", e)
            return JsonResponse({'error': f"error unable to log out : {e}"},
                                status=401)
    else:
        return JsonResponse({'error': 'user not log'}, status=401)
