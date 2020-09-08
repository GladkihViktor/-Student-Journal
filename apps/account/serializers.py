from rest_framework import serializers

from account.models import User
from utils.serializers import PasswordMixin


class UserSerializer(serializers.ModelSerializer, PasswordMixin):
    """User serializer"""
    birthday = serializers.DateField(required=True)
    
    
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name',
                  'second_name', 'last_name', 'birthday')
    
    
    def create(self, validated_data):
        """Create method for User-student
        """
        model = self.Meta.model
        instance = model.objects.create_student(**validated_data)
        return instance
