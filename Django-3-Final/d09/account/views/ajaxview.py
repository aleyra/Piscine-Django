from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render
from d09.tools import isAjaxCustom, print_rouge
from time import time


class AjaxHandlerView(View):
    def get(self, request):
        text = request.GET.get("button_text")

        if isAjaxCustom(request):
            t = time()
            if text:
                print_rouge(text)
            return JsonResponse({"seconds": t}, status=200)
        else:
            return render(request, "account/ajax.html")

    def post(self, request):
        card_text = request.POST.get("text")

        result = f"I've got : {card_text}"
        return JsonResponse({"data": result}, status=200)