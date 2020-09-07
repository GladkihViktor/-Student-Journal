from django.contrib.auth.models import AbstractUser, \
    UserManager as AbstractUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseMixin


class UserManager(AbstractUserManager):
    """User manager."""
    
    def create_superuser(self, email: str, username: str = None,
                         password: str = None, **extra_fields):
        if username is None:
            username = email
        return super().create_superuser(
            username=username, email=email, password=password, **extra_fields)


class UserQuerySet(models.QuerySet):
    """User queryset"""
    
    def students(self) -> models.QuerySet:
        self.filter(is_student=True)
    
    def active_by_email(self, email: str) -> models.QuerySet:
        return self.filter(email=email, is_active=True)


class User(AbstractUser, BaseMixin):
    """User model."""
    email = models.EmailField(_('email address'), blank=False, null=False,
                              unique=True)
    second_name = models.CharField(_('second name'), max_length=150, blank=True)
    is_student = models.BooleanField(_('is student'), default=False,
                                     blank=False, null=True)
    birthday = models.DateField(blank=True, null=True, default=None,
                                verbose_name=_('birthday'))
    
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
