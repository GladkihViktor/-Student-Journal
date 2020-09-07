from django.test import RequestFactory, TestCase

from account.models import User
from authorization.views import LoginWithToken
from utils.tests import student_test as user


class TestLogin(TestCase):
    """Test login view"""
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_student(email=user.email,
                                                password=user.password,
                                                first_name=user.first_name,
                                                second_name=user.second_name,
                                                last_name=user.last_name)
    
    def test_login(self):
        test = {'email': user.email,
                'password': user.password}
        request = self.factory.post('api/authorization/login/', data=test)
        response = LoginWithToken.as_view()(request)
        self.assertEqual(response.status_code, 200)

