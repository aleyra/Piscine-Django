from django import forms


class Name(forms.Form):
    name = forms.CharField(label="Your name")


class Password(forms.Form):
    password = forms.CharField(label="Your password")


class PasswordConfirmation(forms.Form):
    password_confirmation = forms.CharField(label="Password confirmation")