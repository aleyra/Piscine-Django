def print_rouge(s):
    print("\033[91m" + s + "\033[00m")


# https://testdriven.io/blog/django-ajax-xhr/

# equivalent a is_ajax()
def isAjaxCustom(request):
    # return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'  # ca marche aussi
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'