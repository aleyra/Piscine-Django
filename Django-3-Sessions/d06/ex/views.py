from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, get_user_model
from .forms import Name, Password, PasswordConfirmation, TipForm
from ex.models import Tip
from d06.settings import ANONIMOUS_ALIASES

User = get_user_model()

# # Create your views here.

def print_rouge(s):
    print("\033[91m" + s + "\033[00m")

def index(request):
    context = {'alias': request.session['name']}
    return render(request, "ex/index.html", context)


def registration(request):
    context = {
        'form_name': Name(),
        'from_pwd': Password(),
        'form_pwd_conf': PasswordConfirmation(),
        'message': "Choose a username and a password"
    }

    if 'is_authenticated' in request.session.keys() and request.session['is_authenticated'] == "True":
        return HttpResponseRedirect(reverse('index'))

    if request.method == "POST":
        name = Name(request.POST)
        pwd = Password(request.POST)
        pwd_conf = PasswordConfirmation(request.POST)
        if (
            name.is_valid() and pwd.is_valid() and pwd_conf.is_valid()
        ):
            name = name.cleaned_data['name']
            pwd = pwd.cleaned_data['password']
            pwd_conf = pwd_conf.cleaned_data['password_confirmation']
            
            if pwd == pwd_conf:
                # try:
                if User.objects.filter(username=name).exists() or name in ANONIMOUS_ALIASES:
                    message = f"{name} is not available, choose another one"
                    context.update({'message': message})
                    return render(request, "ex/registration.html", context)
                else:
                    row = User(username=name)
                    row.set_password(pwd)
                    row.save()
                    return HttpResponse(f"user {name} created")
                # except Exception as err:
                #     message = f'Error: {err}'
                #     context.update({'message': message})
                #     return render(request, "ex/registration.html", context)
            else:
                message = "You haven't enter the same password for confirmation"
                context.update ({'message': message})
                return render(request, "ex/registration.html", context)
    return render(request, "ex/registration.html", context)

def login(request):
    context = {
        'form_name': Name(),
        'form_pwd': Password(),
        'message': "Please Log in"
    }
    if request.user.is_authenticated == True:
        return HttpResponseRedirect(reverse('index'))
    if request.method == "POST":
        name = Name(request.POST)
        pwd = Password(request.POST)
        
        if name.is_valid() and pwd.is_valid():
            print_rouge("1e ok")
            name = name.cleaned_data['name']
            pwd = pwd.cleaned_data['password']
            print_rouge(f"{name} {pwd}")
            user = authenticate(username=name, password=pwd)
            if user is not None:
                print_rouge("2e ok")
                request.session['name'] = name
                return HttpResponse(f"user {name} connected")
            else:
                print_rouge("2e nok")
                message = f'Wrong password or username'
                context.update({'message': message})
                return render(request, "ex/login.html", context)
    #         print_rouge(f"{name}\n{pwd}")
    #         try:
    #             if User.objects.filter(username=name).exists():
    #                 print_rouge("ici")
    #                 row = User.objects.get(username=name)
    #                 if row.password != pwd:
    #                     message = f'Wrong password'
    #                     context.update({'message': message})
    #                     return render(request, "ex/login.html", context)
    #                 print_rouge("pwd ok")
    #                 print(dir(request.user))
    #                 request.user.is_authenticated = True
    #                 request.session['name'] = row.username
    #                 return render(request, "ex/login.html", context)
    #             else:
    #                 message = f'Wrong username'
    #                 context.update({'message': message})
    #                 return render(request, "ex/login.html", context)
    #         except Exception as err:
    #             message = f'Error: {err}'
    #             context.update({'message': message})
    #             return render(request, "ex/login.html", context)
    return render(request, "ex/login.html", context)


def logout(request):
    request.session.flush()
    # request.user.is_authenticated == False
    return HttpResponseRedirect(reverse('index'))


def display(request):
    try:
        user_lst = User.objects.all().values()
    except Exception as err:
        return HttpResponse(f"No data available because: {err}")
    return render(request, f"ex/display.html", {'user_lst': user_lst})


def tips(request):
    context = {
        'alias': request.session['name'],
        'tip_lst': [],
        'form_tip': TipForm(),
        'message': "List of Tips",
        # 'is_authenticated': 'False'
    }

    # if (
    #     request.user.is_authenticated == True
    # ):
    #     context.update({'is_authenticated': 'True'})

    try:
        tip_lst = Tip.objects.all().values()
        context.update({'tip_lst': tip_lst})
    except Exception as err:
        message = f"No data available because: {err}"
        context.update({'message': message})
        return render(request, "ex/index.html", context)
    if request.method == "POST":
        tip = TipForm(request.POST)
        if tip.is_valid():
            tip = tip.cleaned_data
            row = Tip(**tip)
            row.author = request.session['name']
            row.save()
            message = f"tip : {tip['content']} by {tip['author']} at {tip['date']} saved"
            context.update({'message': message})
            return render(request, "ex/index.html", context)
        
    
    return render(request, "ex/index.html", context)