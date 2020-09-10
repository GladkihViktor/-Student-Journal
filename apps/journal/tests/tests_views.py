from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User
from journal.models import Journal, Program
from utils.tests import (program_test as program,
                         program_test2 as program2,
                         student_test as user,
                         teacher_test as teacher)


class TestJournalViews(APITestCase):
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
        
        self.program = Program(name=program.name)
        self.program.save()
        self.journal = Journal(student=self.student, program=self.program,
                               value=3)
        self.journal.save()
        token, created = Token.objects.get_or_create(user=self.teacher)
        self.http_authorization = 'Token {}'.format(token)
    
    def test_create_program(self):
        test = {'name': program2.name}
        url = reverse('api:journal:list-create-program')
        response = self.client.post(url, data=test,
                                    HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_program(self):
        url = reverse('api:journal:list-create-program')
        response = self.client.get(url,
                                   HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_program(self):
        test = {'name': 'Updated name'}
        url = reverse('api:journal:retrieve-update-program',
                      args=[self.program.id])
        response = self.client.patch(url, data=test,
                                     HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_program(self):
        url = reverse('api:journal:retrieve-update-program',
                      args=[self.program.id])
        response = self.client.get(url,
                                   HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_journal(self):
        test = {'student': self.student.id,
                'program': self.program.id,
                'value': 2}
        url = reverse('api:journal:list-create-journal')
        response = self.client.post(url, data=test,
                                    HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_journal(self):
        url = reverse('api:journal:list-create-journal')
        response = self.client.get(url,
                                   HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_journal(self):
        test = {'value': 4}
        url = reverse('api:journal:retrieve-update-journal',
                      args=[self.journal.id])
        response = self.client.patch(url, data=test,
                                     HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_journal(self):
        url = reverse('api:journal:retrieve-update-journal',
                      args=[self.journal.id])
        response = self.client.get(url,
                                   HTTP_AUTHORIZATION=self.http_authorization)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
