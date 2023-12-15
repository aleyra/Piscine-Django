from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, get_user_model, logout, login
from .forms import TipForm, TipActionForm
# from .forms import RegisterForm
from .forms import Name, Password, PasswordConfirmation
from ex.models import Tip, Vote
from d06.settings import ANONIMOUS_ALIASES

User = get_user_model()

context = {
    'form_name': Name(),
    'form_pwd': Password(),
    'form_pwd_conf': PasswordConfirmation(),
    'alias': '',
    'tip_lst': [],
    'form_tip': TipForm(),
    'message': ""
}

# # Create your views here.

def print_rouge(s):
    print("\033[91m" + s + "\033[00m")

def home(request):
    print_rouge('--home--')
    print(request)
    context = {
        'request': request,
        'alias': request.session['name'],
        }
    return render(request, "ex/home.html", context)


def register(request):
    context.update({'message': "Choose a username and a password"})

    if 'is_authenticated' in request.session.keys() and request.session['is_authenticated'] == "True":
        return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        name = Name(request.POST)
        pwd = Password(request.POST)
        pwd_conf = PasswordConfirmation(request.POST)
        # register = RegisterForm(request.POST)
        if (
            name.is_valid() and pwd.is_valid() and pwd_conf.is_valid()
            # register.is_valid()
        ):
            name = name.cleaned_data['name']
            pwd = pwd.cleaned_data['password']
            pwd_conf = pwd_conf.cleaned_data['password_confirmation']
            # register = register.cleaned_data
            
            if pwd == pwd_conf:
            # if register['password'] == register['password_confirm']:
                # try:
                if (
                    User.objects.filter(username=name).exists()
                    or name in ANONIMOUS_ALIASES
                ):
                    message = f"{name} is not available, choose another one"
                    context.update({'message': message})
                    return render(request, "ex/register.html", context)
                else:
                    row = User(username=name)
                    row.set_password(pwd)
                    row.save()
                    return HttpResponse(f"user {name} created")
                # except Exception as err:
                #     message = f'Error: {err}'
                #     context.update({'message': message})
                #     return render(request, "ex/register.html", context)
            else:
                message = "You haven't enter the same password for confirmation"
                context.update ({'message': message})
                return render(request, "ex/register.html", context)
    return render(request, "ex/register.html", context)


def login(request):
    context.update({'message': "Please Log in"})
    
    if request.user.is_authenticated == True:
        return HttpResponseRedirect(reverse('home'))
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
                login(request, user)
                print(user)
                print_rouge("2e ok")
                # request.session['name'] = name
                return HttpResponseRedirect(reverse('home'))
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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def tips(request):
    context.update({'message': "List of Tips", 'alias': request.session['name']})

    try:
        tip_lst = Tip.objects.all().values()
        context.update({'tip_lst': tip_lst})
    except Exception as err:
        message = f"No data available because: {err}"
        context.update({'message': message})
        return render(request, "ex/home.html", context)
    if request.method == "POST":
        tip = TipForm(request.POST)
        if tip.is_valid():
            tip = tip.cleaned_data
            row = Tip(**tip)
            row.author = 'anonymous'
            # row.author = request.session['name']
            row.save()
            message = f"tip : {tip['content']} saved"
            context.update({'message': message})
            return render(request, "ex/home.html", context)
        else:
            message = "Try again"
            context.update({'message': message})
            return render(request, "ex/home.html", context)
    
    return render(request, "ex/home.html", context)


def vote(tip: Tip, user: User, which_one):
    if Vote.objects.filter(username=user.username, tip_id=tip.id).exists():
        vote = Vote.objects.get(username=user.username, tip_id=tip.id)
        if vote.vote == -1:
            tip.downvote -= 1
            if which_one == 'up':
                tip.upvote += 1
                vote.vote = 1
            else:
                vote.delete()
        if vote.vote == 1:
            tip.upvote -= 1
            if which_one == 'down':
                tip.downvote += 1
                vote.vote = -1
            else:
                vote.delete()
    else:
        print("bouh")



def tip_action(request):
    tip = None
    user = None
    if request.method == 'POST':
        form = TipActionForm(request.POST)
        if form.is_valid():
            tip_id = form.cleaned_data['id']
  
            try: 
                tip = Tip.objects.get(id=tip_id)
                user = User.objects.get(name=request.session['name'])
                if tip is None or user is None:
                    raise Exception("Tip or User is None")
            except Exception as e:
                context.update({'message': f"ERROR : {e}"})
                return HttpResponseRedirect(reverse('home'))
            print_rouge(f"tip = {tip}")
            if 'upvote' in request.POST:
                print_rouge(f"UPVOTE TIP {tip_id}")
                vote(tip, user, 'up')
            elif 'downvote' in request.POST:
                print(f"DOWNVOTE TIP {tip_id}")
                vote(tip, user, 'down')
            elif 'delete' in request.POST:
                print(f"DELETE TIP {tip_id}")
                delete_tip(tip)

    return HttpResponseRedirect(reverse('home'))