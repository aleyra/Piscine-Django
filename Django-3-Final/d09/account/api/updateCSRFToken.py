from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_protect
from d09.tools import print_rouge


@require_GET
@csrf_protect
def updateCSRFToken(request):
    new_token = get_token(request)
    print_rouge(f"tokenUpdated : {new_token}")
    return JsonResponse({'newToken': new_token})