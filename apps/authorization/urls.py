"""Swagger views."""
from django.urls import path

from .views import LoginWithToken

urlpatterns = [
    path(route='login/', view=LoginWithToken.as_view(),
         name='login-with-token'),
]
