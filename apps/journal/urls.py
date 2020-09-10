from django.urls import path
from journal.views import ProgramView, ProgramDetailView

urlpatterns = [
    path(route='program/', view=ProgramView.as_view(),
         name='list-create-program'),
    path(route='program/<int:pk>/', view=ProgramDetailView.as_view(),
         name='retrieve-update-program'),
]
