from dataclasses import dataclass
from datetime import date


@dataclass
class UserData:
    email: str
    password: str
    first_name: str
    second_name: str
    second_name: str
    last_name: str
    birthday: date


student_test = UserData(email='test@gmai.com',
                        password='test',
                        first_name='First test name',
                        second_name='Second test name',
                        last_name='Test last name',
                        birthday=date(1993, 3, 11)
                        )

superuser_test = UserData(email='super@gmai.com',
                          password='super',
                          first_name='First',
                          second_name='Second',
                          last_name='Last',
                          birthday=date(1993, 3, 11)
                          )

student2_test = UserData(email='test2@gmai.com',
                         password='test2',
                         first_name='First test name2',
                         second_name='Second test name2',
                         last_name='Test last name2',
                         birthday=date(1993, 3, 11)
                         )

teacher_test = UserData(email='teacher@gmai.com',
                        password='teacher',
                        first_name='Teacher name',
                        second_name='Teacher second name',
                        last_name='Teacher last name',
                        birthday=date(1983, 2, 1)
                        )
