from django import forms

# https://www.geeksforgeeks.org/choicefield-django-forms/

class RemoveForm(forms.Form): 
    title = forms.ChoiceField(choices=(), required=True)

    def __init__(self, choices, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['title'].choices = choices  # on recup/reorganise les titles pour les mettre ds choices 