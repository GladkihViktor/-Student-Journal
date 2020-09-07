"""Swagger views."""
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly

schema_view = get_schema_view(
    openapi.Info(
        title='Student Journal API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    re_path(r'^docs(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui(cache_timeout=0),
            name='schema-swagger-ui')
]
