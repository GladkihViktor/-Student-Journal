from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from journal.models import Journal, Program
from journal.permissions import TeacherPermission
from journal.serializers import JournalSerializer, ProgramSerializer


class ProgramView(ListCreateAPIView):
    """Program base view for create and list."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [TeacherPermission, IsAuthenticated]


class ProgramDetailView(RetrieveUpdateAPIView):
    """Program detail view for read and update."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [TeacherPermission, IsAuthenticated]


# TODO: Add filters by student and program
class JournalView(ListCreateAPIView):
    """Journal base view for create and list."""
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [TeacherPermission, IsAuthenticated]


class JournalDetailView(RetrieveUpdateAPIView):
    """Journal detail view for read and update."""
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [TeacherPermission, IsAuthenticated]
