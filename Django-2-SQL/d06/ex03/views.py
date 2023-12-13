from django.shortcuts import render
from django.http import HttpResponse

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
    match request.path:
        case '/ex02/display/':
            ex_name = 'ex02'
        case '/ex03/display/':
            ex_name = 'ex03'
        case '/ex04/display/':
            ex_name = 'ex04'
    try:
        movies_lst = Movies.objects.all().values()
        # print(movies_lst)
    except Exception as err:
        return HttpResponse(f"No data available because: {err}")
    return render(request, "{ex_name}/table.html", {'movies_lst': movies_lst})