from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from d04 import settings

import logging

from .forms import History


def my_form(request):
    logger = logging.getLogger('ex02')  # c'est ce qui va gerer les log de l'historique
    
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # form = Form(request.POST)
        form = History(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            logger.info(form.cleaned_data['history'])
            # redirect to a new URL:
            return HttpResponseRedirect("/ex02")

    try:
        f = open(settings.HISTORY_LOG_FILE, 'r')
        histories = [lines for lines in f.readlines()]
    except:
        histories = []
    return render(request, "ex02/form.html", {"form": History(), 'histories': histories})