from django import forms


class History(forms.Form):
    history = forms.CharField(label="Your history")