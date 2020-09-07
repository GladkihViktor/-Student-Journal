from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class BaseMixin(models.Model):
    """ Base mixin for models.
    Add created and modified fields."""
    
    created = models.DateTimeField(default=timezone.now, editable=False,
                                   verbose_name=_('Date created'))
    modified = models.DateTimeField(auto_now=True,
                                    verbose_name=_('Date updated'))
    
    
    class Meta:
        abstract = True
