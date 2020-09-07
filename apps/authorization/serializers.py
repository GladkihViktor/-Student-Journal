from typing import Optional

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from account.models import User


def authenticate(**credentials) -> Optional[User]:
    """
    If the given credentials are valid, return a User object.
    """
    email = credentials.get('email')
    password = credentials.get('password')
    user = User.objects.active_by_email(email=email).first()
    if user.check_password(password):
        return user
    return None


class TokenSerializer(serializers.Serializer):
    """Tokem serializer.
    Validate email and password and return token"""
    
    token = serializers.CharField(label=_("token"), read_only=True)
    email = serializers.CharField(label=_("email"))
    password = serializers.CharField(
        label=_("password"),
        style={'input_type': 'password'},
        trim_whitespace=False, write_only=True
    )
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            user = authenticate(email=email, password=password)
            
            # The authenticate call simply returns None for is_active=False
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        
        token, created = Token.objects.get_or_create(user=user)
        
        attrs['token'] = token
        return attrs
