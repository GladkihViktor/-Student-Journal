from django.test import RequestFactory, TestCase

from account.models import User
from authorization.views import LoginWithToken, SigInView
from utils.tests import student2_test as user2, student_test as user


class TestAuthorization(TestCase):
    """Test Authorization views"""
    
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
    
    def test_sigin(self):
        test = {'email': user2.email,
                'password': user2.password,
                'first_name': user2.first_name,
                'second_name': user2.second_name,
                'last_name': user2.last_name,
                'birthday': user2.birthday}
        request = self.factory.post('api/authorization/sigin/', data=test)
        response = SigInView.as_view()(request)
        self.assertEqual(response.status_code, 201)
    
    def test_sigin_exists(self):
        test = {'email': user.email,
                'password': user.password,
                'first_name': user.first_name,
                'second_name': user.second_name,
                'last_name': user.last_name,
                'birthday': user.birthday}
        request = self.factory.post('api/authorization/sigin/', data=test)
        response = SigInView.as_view()(request)
        self.assertEqual(response.status_code, 400)
