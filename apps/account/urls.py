from django.urls import path

from account.views import UserList

urlpatterns = [
    path(route='', view=UserList.as_view(),
         name='list-users'),
]
