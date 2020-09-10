from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class PasswordMixin(metaclass=serializers.SerializerMetaclass):
    """Password mixin"""
    password = serializers.CharField(
        label=_("password"),
        style={'input_type': 'password'},
        trim_whitespace=False, write_only=True
    )


class BaseMixin(metaclass=serializers.SerializerMetaclass):
    """Base mixin"""
    created = serializers.DateTimeField(label=_('created'), read_only=True)
    modified = serializers.DateTimeField(label=_('modified'), read_only=True)
