from django.shortcuts import render
from django.http import HttpResponse

from d06.tools import ex_name
from ex02.views import movies
from ex03.models import Movies


# https://www.w3schools.com/django/django_insert_data.php

def populate(request):
    response = ""
    for movie in movies:
        try:
            row = Movies(**movie)
            row.save()
            response += f"{movie['title']}: saved<br \>"
        except Exception as err:
            response += f"{movie['title']}: {err}<br \>"
    return HttpResponse(response)

def display(request):
    ex_nb = ex_name(request)

    try:
        movies_lst = Movies.objects.all().values()
        # print(movies_lst)
    except Exception as err:
        return HttpResponse(f"No data available because: {err}")
    return render(request, f"{ex_nb}/table.html", {'movies_lst': movies_lst})