from django.contrib.auth.models import (AbstractUser,
                                        UserManager as AbstractUserManager)
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseMixin


class UserManager(AbstractUserManager):
    """User manager."""
    
    use_in_migrations = False
    
    def create_student(self, email: str, password: str, first_name: str,
                       second_name: str, last_name: str, **extra_fields):
        extra_fields.setdefault('is_student', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        extra_fields['first_name'] = first_name
        extra_fields['second_name'] = second_name
        extra_fields['last_name'] = last_name
        
        return self._create_user(username=email, email=email,
                                 password=password, **extra_fields)
    
    def create_teacher(self, email: str, password: str, first_name: str,
                       second_name: str, last_name: str, **extra_fields):
        extra_fields.setdefault('is_student', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_teacher', True)
        
        extra_fields['first_name'] = first_name
        extra_fields['second_name'] = second_name
        extra_fields['last_name'] = last_name
        
        return self._create_user(username=email, email=email,
                                 password=password, **extra_fields)
    
    def create_superuser(self, email: str, username: str = None,
                         password: str = None, **extra_fields):
        if username is None:
            username = email
        return super().create_superuser(
            username=username, email=email, password=password, **extra_fields)


class UserQuerySet(models.QuerySet):
    """User queryset."""
    
    def available(self) -> models.QuerySet:
        return self.filter(Q(is_student=True) | Q(is_teacher=True),
                           is_student=True)
    
    def students(self) -> models.QuerySet:
        return self.filter(is_student=True)
    
    def teachers(self) -> models.QuerySet:
        return self.filter(is_teacher=True)
    
    def active_by_email(self, email: str) -> models.QuerySet:
        return self.filter(email=email, is_active=True)


class User(AbstractUser, BaseMixin):
    """User model."""
    email = models.EmailField(_('Email address'), blank=False, null=False,
                              unique=True)
    second_name = models.CharField(_('Second name'), max_length=150, blank=True)
    is_student = models.BooleanField(_('Is student'), default=False,
                                     blank=False, null=True)
    is_teacher = models.BooleanField(_('Is teacher'), default=False,
                                     blank=False, null=False)
    birthday = models.DateField(blank=True, null=True, default=None,
                                verbose_name=_('Birthday'))
    
    objects = UserManager.from_queryset(UserQuerySet)()
    
    def get_full_name(self):
        """
        Return the first_name plus the second_name and plus the last_name
        with a space in between.
        """
        full_name = '%s %s %s' % (self.first_name, self.second_name,
                                  self.last_name)
        return full_name.strip()
    
    
    class Meta:
        unique_together = ('first_name', 'second_name', 'last_name',
                           'birthday', 'email')
