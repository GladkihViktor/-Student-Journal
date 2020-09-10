from rest_framework.serializers import ModelSerializer
from journal.models import Journal, Program
from utils.serializers import BaseMixin


class ProgramSerializer(BaseMixin, ModelSerializer):
    """Program serializer"""
    class Meta:
        model = Program
        fields = ('id', 'name', 'is_active', 'created', 'modified')


class JournalSerializer(ModelSerializer):
    """"""
    class Meta:
        model = Journal
