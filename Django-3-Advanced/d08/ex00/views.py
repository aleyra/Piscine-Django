from django.views.generic import RedirectView, FormView, ListView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm
from .models import Article
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages

class HomeView(RedirectView):
    pattern_name = 'articles'
    url = reverse_lazy(pattern_name)

class LoginView(FormView):
    template_name = "ex00/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get(self, request: HttpRequest,
            *args: str, **kwargs) -> HttpResponse:
        if self.request.user.is_authenticated:
            messages.error(self.request, 'already logged in')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: LoginForm):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request,
                            username=username,
                            password=password)
        if user is None:
            messages.error(self.request,
                           "You have entered an invalid username or password")
            return None
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class ArticlesView(ListView):
    model = Article
    template_name = 'ex00/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
    def get_queryset(self):
        return Article.objects.filter().order_by('-created')
