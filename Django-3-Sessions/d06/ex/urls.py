from django.urls import path, include

from . import views
# from .views import SignUpView


urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("display/", views.display, name="display"),
    # path("registration/", SignUpView.as_view(), name="registration"),
    # path("login/", SignUpView.as_view(), name="login"),
]
