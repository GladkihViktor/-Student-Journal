from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User
from utils.tests import student2_test as user2, student_test as user, \
    teacher_test as teacher


class TestAuthorization(APITestCase):
    """Test Authorization views"""
    
    def setUp(self):
        self.student = User.objects.create_student(email=user.email,
                                                   password=user.password,
                                                   first_name=user.first_name,
                                                   second_name=user.second_name,
                                                   last_name=user.last_name)
        
        self.teacher = User.objects.create_teacher(email=teacher.email,
                                                   password=teacher.password,
                                                   first_name=teacher.first_name,
                                                   second_name=teacher.second_name,
                                                   last_name=teacher.last_name)
        
        token, created = Token.objects.get_or_create(user=self.teacher)
        self.http_authorization = 'Token {}'.format(token)
    
    def test_create(self):
        test = {'email': user2.email,
                'password': user2.password,
                'first_name': user2.first_name,
                'second_name': user2.second_name,
                'last_name': user2.last_name,
                'birthday': user2.birthday}
        url = reverse('api:account:list-create-users')
        response = self.client.post(url, data=test,
                                    HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list(self):
        url = reverse('api:account:list-create-users')
        response = self.client.get(url,
                                   HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update(self):
        test = {'first_name': 'Updated name'}
        url = reverse('api:account:rud-user',
                      args=[self.student.id])
        response = self.client.patch(url, data=test,
                                     HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve(self):
        url = reverse('api:account:rud-user', args=[self.student.id])
        response = self.client.get(url,
                                   HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete(self):
        url = reverse('api:account:rud-user', args=[self.student.id])
        response = self.client.delete(url,
                                      HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
