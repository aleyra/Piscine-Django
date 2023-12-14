from django import forms
from django.forms import ModelForm
from ex.models import Tip


class Name(forms.Form):
    name = forms.CharField(label="Your name")


class Password(forms.Form):
    password = forms.CharField(label="Your password")


class PasswordConfirmation(forms.Form):
    password_confirmation = forms.CharField(label="Password confirmation")


# Create the form class.
# https://docs.djangoproject.com/fr/4.2/topics/forms/modelforms/
class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = ["content", "author", "date"]