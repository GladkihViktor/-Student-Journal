from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from journal.models import Program
from journal.permissions import TeacherPermission
from journal.serializers import ProgramSerializer


class ProgramView(ListCreateAPIView):
    """Journal base view for create and list"""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [TeacherPermission, IsAuthenticated]


class ProgramDetailView(RetrieveUpdateAPIView):
    """"""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [TeacherPermission, IsAuthenticated]
