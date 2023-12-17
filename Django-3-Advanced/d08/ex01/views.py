from django.shortcuts import render
from ex00.models import Article, UserFavouriteArticle
from django.views.generic import DetailView, RedirectView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import logout
from django.urls import reverse_lazy

# Create your views here.

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'ex01/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Article Detail'

        if self.request.user.is_authenticated:
            is_favourite = UserFavouriteArticle.objects.filter(
                user=self.request.user,
                article=self.get_object()
            ).exists()
            context['isFavourite'] = is_favourite

        return context
    
@method_decorator(login_required, name='dispatch')
class FavouritesView(ListView):
    template_name = "ex01/favourites.html"
    model = UserFavouriteArticle

    def get_queryset(self):
        return self.model.objects \
               .filter(user=self.request.user)

class LogoutView(RedirectView):
    url = reverse_lazy('articles')

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class PublicationsView(ListView):
    template_name = "ex01/publications.html"
    model = Article

    def get_queryset(self):
        return Article.objects \
                      .filter(author=self.request.user.id) \
                      .order_by('-created')