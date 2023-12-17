from django.urls import path
from .views import HomeView, ArticlesView, LoginView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path("login/", LoginView.as_view(), name="login"),
]