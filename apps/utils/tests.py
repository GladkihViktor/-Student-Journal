from dataclasses import dataclass


@dataclass
class UserData:
    email: str
    password: str
    first_name: str
    second_name: str
    second_name: str
    last_name: str


student_test = UserData(email='test@gmai.com',
                        password='test',
                        first_name='First test name',
                        second_name='Second test name',
                        last_name='Test last name')

superuser_test = UserData(email='super@gmai.com',
                          password='super',
                          first_name='First',
                          second_name='Second',
                          last_name='Last')
