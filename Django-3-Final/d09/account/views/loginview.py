class LoginView(FormView):
    template_name = "account/account.html"
    form_class = LoginForm
    success_url = reverse_lazy('login')
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
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

    def form_valid(self, form):
        if isAjaxCustom(self.request):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(self.request,
                                username=username,
                                password=password)
            if user is None:
                return JsonResponse({"message": "invalid credentials"},
                                    status=400)
            login(self.request, user)
            print_rouge(f"LOGGED AS {username}.")
            return JsonResponse({"message": "success"}, status=200)
        else:
            print_rouge("Error : form_valid called without ajax")

    def form_invalid(self, form):
        if isAjaxCustom(self.request):
            print_rouge(f"INVALID FORM : {form.errors}")
            return JsonResponse({"message": f"error invalid form {form.errors}"},
                                status=400)
        else:
            print_rouge("Error : form_invalid called without ajax")
            return super().form_invalid(form)