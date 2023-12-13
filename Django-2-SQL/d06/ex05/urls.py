from django.urls import path

from . import views
from ex03 import views as views3

urlpatterns = [
    path("populate/", views3.populate, name="populate"),
    path("display/", views3.display, name="display")
]
