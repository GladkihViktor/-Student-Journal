from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseMixin


class Program(BaseMixin):
    """Training program."""
    name = models.CharField(max_length=256, null=False, blank=False,
                            verbose_name=_('name'), unique=True)
    is_active = models.BooleanField(default=True, blank=False, null=False,
                                    verbose_name=_('Is active'))
    
    
    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')

#TODO: Может добавлять только пользователь teacher
class Journal(BaseMixin):
    """Journal for the records students rating."""
    
    VERY_BAD = 1
    BAD = 2
    NORMAL = 3
    GOOD = 4
    EXCELLENT = 5
    
    VALUE_CHOICES = (
        (VERY_BAD, _('Very bad')),
        (BAD, _('Bad')),
        (NORMAL, _('Normal')),
        (GOOD, _('Good')),
        (EXCELLENT, _('Excellent'))
    )
    
    program = models.ForeignKey('Program', on_delete=models.PROTECT,
                                verbose_name=_('Program'))
    student = models.ForeignKey('account.User', on_delete=models.CASCADE,
                                verbose_name=_('Student'))
    value = models.IntegerField(choices=VALUE_CHOICES, null=False,
                                blank=False, verbose_name=_('Value'))
    
    
    class Meta:
        verbose_name = _('Journal')
        verbose_name_plural = _('Journals')
