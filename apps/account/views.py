from rest_framework.generics import ListCreateAPIView

from account.models import User
from account.permissions import UserPermission
from account.serializers import UserSerializer


class UserList(ListCreateAPIView):
    queryset = User.objects.available()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
