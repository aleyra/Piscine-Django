from django.shortcuts import render
# from django.http import HttpResponse


def my_table(request):
    step = 255 / 50
    context = {
        "range": [
            "{:02X}".format(int(i * step)) for i in range(50)
        ]
    }
    return render(request, "ex03/table.html", context)