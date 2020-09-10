from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseMixin


class ProgramQuerySet(models.QuerySet):
    
    def available(self) -> models.QuerySet:
        return self.filter(is_active=True)


class Program(BaseMixin):
    """Training program."""
    name = models.CharField(max_length=256, null=False, blank=False,
                            verbose_name=_('name'), unique=True)
    is_active = models.BooleanField(default=True, blank=False, null=False,
                                    verbose_name=_('Is active'))
    
    objects = models.Manager.from_queryset(ProgramQuerySet)()
    
    
    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')


class JournalQuerySet(models.QuerySet):
    
    def by_student_id(self, student_id: int) -> models.QuerySet:
        return self.filter(student_id=student_id)
    
    def by_program_id(self, program_id: int) -> models.QuerySet:
        return self.filter(program_id=program_id)
    
    def by_value(self, value: int) -> models.QuerySet:
        return self.filter(value=value)


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
    
    objects = models.Manager.from_queryset(JournalQuerySet)()
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.program.is_active is False:
            raise ValidationError("Program is not available.", "program")
        if self.student.is_active is False or self.student.is_student is False:
            raise ValidationError("Student is not available.", "student")
        
        super(Journal, self).save(force_insert, force_update,
                                  using, update_fields)
    
    
    class Meta:
        verbose_name = _('Journal')
        verbose_name_plural = _('Journals')
