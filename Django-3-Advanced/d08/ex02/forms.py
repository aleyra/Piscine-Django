from django import forms
from ex00.models import Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddFavouriteForm(forms.Form):
    article_id = forms\
                .IntegerField(widget=forms.HiddenInput())

class PublishForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",  "password1", "password2")