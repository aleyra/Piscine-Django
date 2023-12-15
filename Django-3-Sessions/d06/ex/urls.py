from django.urls import path, include

from . import views
# from .views import SignUpView


urlpatterns = [
    path("", views.tips, name="index"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("display/", views.display, name="display"),
]
