from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

from account.models import User
from account.serializers import UserSerializer


class UserList(ListCreateAPIView):
    """User list with pagination limit-offset."""
    queryset = User.objects.available()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination


class UserDetail(RetrieveUpdateDestroyAPIView):
    """User detail."""
    queryset = User.objects.available()
    serializer_class = UserSerializer
