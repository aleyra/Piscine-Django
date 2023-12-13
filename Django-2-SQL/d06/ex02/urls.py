from django.urls import path

from . import views
from ex00 import views as views0


urlpatterns = [
    path("init/", views0.init, name="init"),
    path("populate/", views.populate, name="populate"),
    path("display/", views.display, name="display")
]
