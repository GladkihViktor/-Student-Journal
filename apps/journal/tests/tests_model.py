from django.core.exceptions import ValidationError
from django.test import TestCase

from account.models import User
from journal.models import Journal, Program
from utils.tests import (program_test, program_test2, student2_test as student2,
                         student_test as student)


class TestJournal(TestCase):
    
    def _init_user(self, students: list):
        usr = User.objects.create_student(email=student.email,
                                          password=student.password,
                                          first_name=student.first_name,
                                          second_name=student.second_name,
                                          last_name=student.last_name
                                          )
        students.append(usr)
        usr = User.objects.create_student(email=student2.email,
                                          password=student2.password,
                                          first_name=student2.first_name,
                                          second_name=student2.second_name,
                                          last_name=student2.last_name
                                          )
        usr.is_active = False
        usr.save()
        students.append(usr)
    
    def _init_program(self, programs: list):
        program = Program(name=program_test.name)
        program.save()
        programs.append(program)
        
        program = Program(name=program_test2.name, is_active=False)
        program.save()
        programs.append(program)
    
    def setUp(self) -> None:
        self.students = list()
        self.programs = list()
        self.value = 4
        self._init_user(students=self.students)
        self._init_program(programs=self.programs)
    
    def test_valid_record(self):
        try:
            j = Journal(student=self.students[0], program=self.programs[0],
                        value=self.value)
            j.save()
        except Exception as ex:
            self.assert_(False, ex)
        else:
            self.assert_(True)
    
    def test_not_valid_student(self):
        try:
            j = Journal(student=self.students[1], program=self.programs[0],
                        value=self.value)
            j.save()
        except ValidationError:
            self.assert_(True)
        else:
            self.assert_(False)
    
    def test_not_valid_program(self):
        try:
            j = Journal(student=self.students[0], program=self.programs[1],
                        value=self.value)
            j.save()
        except ValidationError:
            self.assert_(True)
        else:
            self.assert_(False)
