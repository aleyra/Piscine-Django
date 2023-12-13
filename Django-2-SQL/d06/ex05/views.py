from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from d06.tools import ex_name
from ex02.views import movies
from ex05.models import Movies
from ex04.form import RemoveForm

# Create your views here.

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
        print(f"\n\n{movies_lst}\n\n")  #
    except Exception as err:
        return HttpResponse(f"No data available because: {err}")
    return render(request, f"{ex_nb}/table.html", {'movies_lst': movies_lst})

def remove(request):
    ex_nb = ex_name(request)

    if request.method == 'GET':
        movies_lst = Movies.objects.all()
        # print(movies_lst)  #
        if len(movies_lst) == 0:
            return HttpResponse("No data available")
        context = {'form': RemoveForm(choices=((movie.title, movie.title) for movie in movies_lst))}
        return render(request, f"{ex_nb}/remove.html", context)
    elif request.method == 'POST':
        title_delete = request.POST.get('title')
        Movies.objects.get(title=title_delete).delete()
        return HttpResponseRedirect(request.path)
