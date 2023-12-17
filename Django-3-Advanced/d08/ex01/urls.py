from django.urls import path
from .views import PublicationsView, ArticleDetailView, LogoutView, FavouritesView

urlpatterns = [
    path("publications/", PublicationsView.as_view(), name="publications"),
    path('articles/<slug:pk>/', ArticleDetailView.as_view(), name='detail'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("favourites/", FavouritesView.as_view(), name="favourites"),
]