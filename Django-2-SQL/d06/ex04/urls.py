from django.urls import path

from . import views
from ex00 import views as views0
from ex02 import views as views2


urlpatterns = [
    path("init/", views0.init, name="init"),
    path("populate/", views2.populate, name="populate"),
    path("display/", views2.display, name="display"),
    path("remove/", views.remove, name="remove"),
]
