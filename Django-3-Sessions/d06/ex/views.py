from django.shortcuts import render

from django.http import HttpResponse
from .forms import Name, Password, PasswordConfirmation
from ex.models import User
from d06.settings import ANONIMOUS_ALIASES

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
                try:
                    if User.objects.filter(username=name).exists() or name in ANONIMOUS_ALIASES:
                        # if name in ANONIMOUS_ALIASES:
                        #     print_rouge("is an ANONIMOUS_ALIASES")
                        # else:
                        #     print_rouge("name exist")
                        message = f"{name} is not available, choose another one"
                        context.update({'message': message})
                        return render(request, "ex/registration.html", context)
                    else:
                        # print_rouge("Let's create")
                        row = User(username=name, password=pwd)
                        row.save()
                        return HttpResponse(f"user {name} created")
                except Exception as err:
                    message = f'Error: {err}'
                    context.update({'message': message})
                    return render(request, "ex/registration.html", context)
            else:
                message = "You haven't enter the same password for confirmation"
                context.update ({'message': message})
                return render(request, "ex/registration.html", context)
    return render(request, "ex/registration.html", context)

def login(request):
    context = {
        'form_name': Name(),
        'from_pwd': Password(),
        'message': "Please Log in"
    }

    if request.method == "POST":
        name = Name(request.POST)
        pwd = Password(request.POST)
        
        if name.is_valid() and pwd.is_valid():
            name = name.cleaned_data['name']
            pwd = pwd.cleaned_data['password']
            print_rouge(f"{name}\n{pwd}")
            try:
                if User.objects.filter(username=name).exists():
                    print_rouge("ici")
                    row = User.objects.get(username=name)
                    print(row)
                    if row.password != pwd:
                        message = f'Wrong password'
                        context.update({'message': message})
                        return render(request, "ex/login.html", context)
                    return render(request, "ex/login.html", context)
                else:
                    message = f'Wrong username'
                    context.update({'message': message})
                    return render(request, "ex/login.html", context)
            except Exception as err:
                message = f'Error: {err}'
                context.update({'message': message})
                return render(request, "ex/login.html", context)
    return render(request, "ex/login.html", context)


def display(request):

    try:
        user_lst = User.objects.all().values()
    except Exception as err:
        return HttpResponse(f"No data available because: {err}")
    return render(request, f"ex/display.html", {'user_lst': user_lst})

# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView

# from .forms import CustomUserCreationForm


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("/login")
#     template_name = "account/registration.html"