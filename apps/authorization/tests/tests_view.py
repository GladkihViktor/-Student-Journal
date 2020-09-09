from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User
from utils.tests import student2_test as student, student_test as user


class TestAuthorization(APITestCase):
    """Test Authorization views"""
    
    def setUp(self):
        self.user = User.objects.create_student(email=user.email,
                                                password=user.password,
                                                first_name=user.first_name,
                                                second_name=user.second_name,
                                                last_name=user.last_name)
    
    def test_login(self):
        test = {'email': user.email,
                'password': user.password}
        url = reverse('api:authorization:login-with-token')
        response = self.client.post(url, data=test)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_sigin(self):
        test = {'email': student.email,
                'password': student.password,
                'first_name': student.first_name,
                'second_name': student.second_name,
                'last_name': student.last_name,
                'birthday': student.birthday}
        url = reverse('api:authorization:sig-in')
        response = self.client.post(url, data=test)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_sigin_exists(self):
        test = {'email': user.email,
                'password': user.password,
                'first_name': user.first_name,
                'second_name': user.second_name,
                'last_name': user.last_name,
                'birthday': user.birthday}
        url = reverse('api:authorization:sig-in')
        response = self.client.post(url, data=test)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_logout(self):
        token, created = Token.objects.get_or_create(user=self.user)
        http_authorization = 'Token {}'.format(token)
        
        url = reverse('api:authorization:logout')
        response = self.client.post(url, HTTP_AUTHORIZATION=http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
