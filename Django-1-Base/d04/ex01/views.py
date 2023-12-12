from django.shortcuts import render
# from django.http import HttpResponse

# 1 def / page
def django(request):
    return render(request, "ex01/django.html")

def affichage(request):
    return render(request, "ex01/affichage.html")

def templates(request):
    return render(request, "ex01/templates.html")