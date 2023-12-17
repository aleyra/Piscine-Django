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
    'form_tip': TipForm(),
    'form_tipaction': TipActionForm(),
    'alias': '',
    'tip_lst': [],
    'message': ""
}

# # Create your views here.

def print_rouge(s):
    print("\033[91m" + s + "\033[00m")

def home(request):
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
        if (
            name.is_valid() and pwd.is_valid() and pwd_conf.is_valid()
        ):
            name = name.cleaned_data['name']
            pwd = pwd.cleaned_data['password']
            pwd_conf = pwd_conf.cleaned_data['password_confirmation']
            
            if pwd == pwd_conf:
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
                    user = authenticate(username=name, password=pwd)
                    if user is not None:
                        login(request, user)
                        return HttpResponseRedirect(reverse('home'))
            else:
                message = "You haven't enter the same password for confirmation"
                context.update ({'message': message})
                return render(request, "ex/register.html", context)
    return render(request, "ex/register.html", context)


def login_view(request):
    context.update({'message': "Please Log in"})
    
    if request.user.is_authenticated == True:
        return HttpResponseRedirect(reverse('home'))
    if request.method == "POST":
        name = Name(request.POST)
        pwd = Password(request.POST)
        
        if name.is_valid() and pwd.is_valid():
            context.update()({'form_name': Name(request.POST)})
            name_res = name.cleaned_data['name']
            pwd_res = pwd.cleaned_data['password']
            user = authenticate(username=name_res, password=pwd_res)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                message = f'Wrong password or username'
                context.update({'message': message})
                return render(request, "ex/login.html", context)
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
            row.author = request.user.username
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
    try:
        if Vote.objects.filter(username=user.username, tip_id=tip.id).exists():
            vote = Vote.objects.get(username=user.username, tip_id=tip.id)
            if vote.vote == -1:
                tip.downvote = tip.downvote - 1
                if which_one == 'up':
                    tip.upvote = tip.upvote + 1
                    vote.vote = 1
                    vote.save()
                else:
                    vote.delete()
            elif vote.vote == 1:
                tip.upvote = tip.upvote - 1
                if which_one == 'down':
                    tip.downvote = tip.downvote + 1
                    vote.vote = -1
                    vote.save()
                else:
                    vote.delete()
        elif which_one == 'up':
            vote = Vote(username=user.username, tip_id=tip.id, vote=1)
            tip.upvote = tip.upvote + 1
            vote.save()
        else:
            vote = Vote(username=user.username, tip_id=tip.id, vote=-1)
            tip.downvote = tip.downvote + 1
            vote.save()
        tip.save()
        context.update({'message': f'{which_one}vote saved'})
    except Exception as err:
        context.update({'message': f"Error: {err}"})


def delete_tip(tip: Tip):
    try:
        Vote.objects.filter(tip_id=tip.id).delete()
        tip.delete()
        context.update({'message': f'Tip deleted'})
    except Exception as err:
        context.update({'message': f"Error: {err}"})


def tip_action(request):
    tip = None
    user = None
    if request.method == 'POST':
        form = TipActionForm(request.POST)
        if form.is_valid():
            tip_id = form.cleaned_data['tip_id']
  
            try: 
                tip = Tip.objects.get(id=tip_id)
                user = User.objects.get(username=request.user.username)
                if tip is None or user is None:
                    raise Exception("Tip or User is None")
            except Exception as e:
                context.update({'message': f"ERROR : {e}"})
                return HttpResponseRedirect(reverse('home'))
            if 'upvote' in request.POST:
                vote(tip, user, 'up')
            elif 'downvote' in request.POST:
                vote(tip, user, 'down')
            elif 'delete' in request.POST:
                delete_tip(tip)

    return HttpResponseRedirect(reverse('home'))