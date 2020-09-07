from django.test import TestCase

from account.models import User
from authorization.serializers import authenticate
from utils.tests import student_test as user


class TestAuthenticate(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        """Load initial data for the TestCase."""
        test_user = User.objects.create_student(email=user.email,
                                                password=user.password,
                                                first_name=user.first_name,
                                                second_name=user.second_name,
                                                last_name=user.last_name)
    
    def test_user_credentials_valid(self):
        result = authenticate(email=user.email, password=user.password)
        self.assertIsInstance(result, User)
    
    def test_user_credentials_not_valid(self):
        result = authenticate(email=user.email, password='1231')
        self.assertIsNone(result)
