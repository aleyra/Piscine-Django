from .random_alias import random_alias

class AnonymousSession42secMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # to know if user is anonymous : not request.user.is_authenticated
        if not request.user.is_authenticated:
            if 'name' not in request.session:
                request.session['name'] = random_alias()

        response = self.get_response(request)
        return response 