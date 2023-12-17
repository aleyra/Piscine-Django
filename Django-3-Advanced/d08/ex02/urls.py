from django.urls import path
from .views import RegisterView, PublishView, add_to_favourites

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("publish/", PublishView.as_view(), name="publish"),
    path("favourites/<int:article_id>/add/",
         add_to_favourites, name="add-favourite"),
]