from django.shortcuts import redirect
from ex00.models import Article, UserFavouriteArticle
from .forms import AddFavouriteForm, PublishForm, RegisterForm
from django.contrib.auth.decorators import login_required

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

# Create your views here.

@login_required
def add_to_favourites(request, article_id):
    form = None
    if request.method == 'POST':
        try:
            form = AddFavouriteForm(request.POST)
            if not form.is_valid() or form.cleaned_data['article_id'] != article_id:
                raise Exception(form.errors)
            already = UserFavouriteArticle.objects.filter(
                user=request.user,
                article=Article.objects.get(pk=article_id)
            ).exists()
            if already:
                raise Exception("Already in favourites")
            UserFavouriteArticle.objects.create(
                user=request.user,
                article_id=form.cleaned_data['article_id']
            )
        except Exception as e:
            pass

    return redirect('favourites')

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class PublishView(CreateView):
    form_class = PublishForm
    success_url = reverse_lazy('publications')
    template_name = 'ex02/publish.html'

    def form_valid(self, form) -> HttpResponse:
        try:
            article = form.save(commit=False)
            article.author = self.request.user
            article.save()
            messages.success(self.request,
                             f"Article {article.title} published")
        except (Exception) as e:
            messages.error(self.request, f"Error publishing article : {e}")
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'ex02/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            form.save()
        except (Exception) as e:
            messages.error(self.request,
                           f"Error creating user : {e}")
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)