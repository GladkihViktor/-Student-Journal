from django.urls import path

from journal.views import JournalDetailView, JournalView, ProgramDetailView, \
    ProgramView

urlpatterns = [
    path(route='', view=JournalView.as_view(), name='list-create-journal'),
    path(route='<int:pk>/', view=JournalDetailView.as_view(),
         name='retrieve-update-program'),
    path(route='program/', view=ProgramView.as_view(),
         name='list-create-program'),
    path(route='program/<int:pk>/', view=ProgramDetailView.as_view(),
         name='retrieve-update-program'),
]
