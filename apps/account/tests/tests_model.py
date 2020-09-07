from django.test import TestCase

from account.models import User
from utils.tests import superuser_test as su, student_test as student


class TestUser(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        """Load initial data for the TestCase."""
        usr = User.objects.create_student(email=student.email,
                                          password=student.password,
                                          first_name=student.first_name,
                                          second_name=student.second_name,
                                          last_name=student.last_name
                                          )
        super_usr = User.objects.create_superuser(email=su.email,
                                                  password=su.password)
        
    def test_student(self):
        usr = User.objects.active_by_email(email=student.email).first()
        if usr.is_student is True and usr.is_staff is False and \
                usr.is_superuser is False:
            self.assert_(True)
        else:
            self.assert_(False)

    def test_superuser(self):
        usr = User.objects.active_by_email(email=su.email).first()
        if usr.is_student is False and usr.is_staff is True and \
                usr.is_superuser is True:
            self.assert_(True)
        else:
            self.assert_(False)
