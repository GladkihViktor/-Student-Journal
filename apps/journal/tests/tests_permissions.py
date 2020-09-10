from django.test import TestCase
from journal.permissions import validate_teachers_method, TEACHER_METHODS
from rest_framework.permissions import SAFE_METHODS

teacher_methods_generator = (method for method in TEACHER_METHODS)
safe_methods_generator = (method for method in SAFE_METHODS)


class TestValidateTeacher(TestCase):
    
    def test_valid_permissions_for_teacher_methods(self):
        for method in teacher_methods_generator:
            if validate_teachers_method(method=method,
                                        is_teacher=True) is False:
                self.assert_(False)
                return
        self.assert_(True)
    
    def test_not_valid_permissions_for_teacher_methods(self):
        for method in teacher_methods_generator:
            if validate_teachers_method(method=method) is True:
                self.assert_(False)
                return
        self.assert_(True)
    
    def test_valid_permissions_for_safe_methods_and_teacher(self):
        for method in safe_methods_generator:
            if validate_teachers_method(method=method,
                                        is_teacher=True) is False:
                self.assert_(False)
                return
        self.assert_(True)
    
    def test_valid_permissions_for_safe_methods_not_teacher(self):
        for method in safe_methods_generator:
            if validate_teachers_method(method=method) is False:
                self.assert_(False)
                return
        self.assert_(True)
