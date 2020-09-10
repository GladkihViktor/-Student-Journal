from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from journal.models import Journal


class StudentFilter(filters.NumberFilter):
    """Filter by student."""
    label = _('student')
    
    def filter(self, queryset: models.QuerySet, value: Optional[int]) \
            -> models.QuerySet:
        if value:
            return queryset.by_student_id(student_id=value)
        return queryset


class ProgramFilter(filters.NumberFilter):
    """Filter by program."""
    label = _('program')
    
    def filter(self, queryset: models.QuerySet, value: Optional[int]) \
            -> models.QuerySet:
        if value:
            return queryset.by_program_id(program_id=value)
        return queryset


class ValueFilter(filters.NumberFilter):
    """Filter by program."""
    label = _('value')
    
    def filter(self, queryset: models.QuerySet, value: Optional[int]) \
            -> models.QuerySet:
        if value:
            return queryset.by_value(value=value)
        return queryset


class JournalFilters(filters.FilterSet):
    """FilterSet for Journal model."""
    student = StudentFilter()
    program = ProgramFilter()
    value = ValueFilter()
    
    
    class Meta:
        model = Journal
        fields = ('student', 'program', 'value')
