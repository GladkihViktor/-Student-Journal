from rest_framework.serializers import ModelSerializer

from journal.models import Journal, Program
from utils.serializers import BaseMixin


class ProgramSerializer(BaseMixin, ModelSerializer):
    """Program serializer"""
    
    
    class Meta:
        model = Program
        fields = ('id', 'name', 'is_active', 'created', 'modified')


# TODO: Add methods for update and create journal records
class JournalSerializer(ModelSerializer):
    """Journal serializer"""
    
    
    class Meta:
        model = Journal
        fields = ('id', 'program', 'student', 'value', 'created', 'modified')
