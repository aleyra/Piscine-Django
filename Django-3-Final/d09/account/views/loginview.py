from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from d09.tools import print_rouge, isAjaxCustom
from account.forms.loginForm import LoginForm


# https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/
# https://stackoverflow.com/questions/37693879/formview-with-get-method-doesnt-show-the-form
class LoginView(FormView):
    template_name = "account/account.html"
    form_class = LoginForm
    success_url = reverse_lazy('login')
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):  # methode classique: appelee quand il y a une request.GET
        if isAjaxCustom(request):
            print_rouge("AJAX login get called")
            if self.request.user.is_authenticated:
                print_rouge("USER ALREADY LOGGED IN")
                return JsonResponse({"message": "USER ALREADY LOGGED IN"},
                                    status=400)
            return JsonResponse({"message": "ajax call"}, status=201)
        else:
            print_rouge("Normal Login get called")
            if self.request.user.is_authenticated:
                print_rouge("USER ALREADY LOGGED IN")
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):  # methode classique: appelee quand il y a une request.POST
        if isAjaxCustom(self.request):
            usrname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(self.request,
                                username=usrname,
                                password=pwd)
            if user is None:
                return JsonResponse({"message": "invalid credentials"},
                                    status=400)
            login(self.request, user)
            print_rouge(f"{usrname} is connected now")
            return JsonResponse({"message": "success"}, status=200)
        else:
            print_rouge("Error : form_valid called without ajax")

    def form_invalid(self, form):
        if isAjaxCustom(self.request):
            print_rouge(f"INVALID FORM : {form.errors}")  # .errors est herite de AuthenticationForm
            return JsonResponse({"message": f"error invalid form {form.errors}"},
                                status=400)
        else:
            print_rouge("Error : form_invalid called without ajax")
            return super().form_invalid(form)
        