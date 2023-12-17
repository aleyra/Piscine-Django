def print_rouge(s):
    print("\033[91m" + s + "\033[00m")


def isAjaxCustom(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'