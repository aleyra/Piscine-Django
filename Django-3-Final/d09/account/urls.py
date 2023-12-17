from django.urls import path
from account.views.ajaxview import AjaxHandlerView
from account.views.loginview import LoginView
from account.api.getUsername import getUsername
from account.api.logout import logout
from account.api.updateCSRFToken import updateCSRFToken


urlpatterns = [
    path("", LoginView.as_view(), name="login"),  # .as_view() est cree automatiquement donc il est important de respecter la nomenclature
    path("getUsername/", getUsername, name="getUsername"),
    path("logout/", logout, name="logout"),
    path("updateCRSFToken/", updateCSRFToken, name="updateCRSFToken"),
    # path("ajax/", AjaxHandlerView.as_view(), name="ajax"),  # for https://www.youtube.com/watch?v=QDdLvImfq_g
]