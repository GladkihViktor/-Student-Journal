"""Swagger views."""
from django.urls import include, path

urlpatterns = [
    path('authorization/',
         include(('authorization.urls', 'authorization'))),
    path('account/', include(('account.urls', 'account')))
]
