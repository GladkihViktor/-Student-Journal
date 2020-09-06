"""Swagger views."""
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly

api_schema_view = get_schema_view(
    openapi.Info(title='Student Journal API', default_version='v1'),
    public=True,
    permission_classes=(IsAuthenticatedOrReadOnly,)
)

urlpatterns = [
    re_path(route=r'^docs(?P<format>\.json|\.yaml)$',
            view=api_schema_view.without_ui(), name='schema-json'),
    path(route='docs/', view=api_schema_view.with_ui('swagger'),
         name='swagger'),
]
