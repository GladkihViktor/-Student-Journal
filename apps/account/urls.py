from django.urls import path

from account.views import UserList, UserDetail

urlpatterns = [
    path(route='', view=UserList.as_view(),
         name='list-create-users'),
    path(route='<int:pk>/', view=UserDetail.as_view(),
         name='rud-user'),
]
