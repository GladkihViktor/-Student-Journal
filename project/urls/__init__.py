"""Project urls."""
import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from project.urls import api, docs

urlpatterns = [
    path('api/', include((api.urlpatterns, 'api')), name='api'),
    path('', include(docs), name='docs')
]

if os.environ.get('SETTINGS_CONFIGURATION') != 'production':
    urlpatterns += path('admin/', admin.site.urls),

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
