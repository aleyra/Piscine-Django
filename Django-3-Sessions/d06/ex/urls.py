from django.urls import path, include

from . import views
# from .views import SignUpView

urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.tips, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("tip_action/", views.tip_action, name="tip_action"),
]
