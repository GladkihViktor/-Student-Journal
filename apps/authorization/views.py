from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account.serializers import UserSerializer
from authorization.serializers import TokenSerializer


class LoginWithToken(ObtainAuthToken):
    """Login with token view.
    Check creds and return token for user.
    
    For login send email and password.
    """
    permission_classes = [AllowAny]
    serializer_class = TokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)


class SigInView(CreateAPIView):
    """Sig in view"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
