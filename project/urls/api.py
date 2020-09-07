"""Swagger views."""
from django.urls import include, path

urlpatterns = [
    path('authorization/', include('authorization.urls'), name='authorization'),
]
