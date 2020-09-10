from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from journal.filters import JournalFilters
from journal.models import Journal, Program
from journal.permissions import TeacherPermission
from journal.serializers import JournalSerializer, ProgramSerializer

_permission_classes = (IsAuthenticated, TeacherPermission)


class ProgramView(ListCreateAPIView):
    """Program base view for create and list."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = _permission_classes


class ProgramDetailView(RetrieveUpdateAPIView):
    """Program detail view for read and update."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = _permission_classes


class JournalView(ListCreateAPIView):
    """Journal base view for create and list."""
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    pagination_class = LimitOffsetPagination
    filter_class = JournalFilters
    permission_classes = _permission_classes


class JournalDetailView(RetrieveUpdateAPIView):
    """Journal detail view for read and update."""
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = _permission_classes
