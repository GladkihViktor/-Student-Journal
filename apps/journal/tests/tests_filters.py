from journal.filters import ProgramFilter, StudentFilter, ValueFilter
from journal.models import Journal
from journal.tests import tests_model


class TestJournalFilter(tests_model.TestJournal):
    """Tests for filter in Journal"""
    
    def setUp(self) -> None:
        super(TestJournalFilter, self).setUp()
        
        jr = Journal(student=self.students[0], program=self.programs[0],
                     value=self.value)
        jr.save()
    
    def test_student_filter(self):
        qs = Journal.objects.all()
        filter_cls = StudentFilter()
        if filter_cls. \
                filter(queryset=qs, value=self.students[0].id).count() > 0:
            self.assert_(True)
        else:
            self.assert_(False)
    
    def test_program_filter(self):
        qs = Journal.objects.all()
        filter_cls = ProgramFilter()
        if filter_cls. \
                filter(queryset=qs, value=self.programs[0].id).count() > 0:
            self.assert_(True)
        else:
            self.assert_(False)
    
    def test_value_filter(self):
        qs = Journal.objects.all()
        filter_cls = ValueFilter()
        if filter_cls. \
                filter(queryset=qs, value=self.value).count() > 0:
            self.assert_(True)
        else:
            self.assert_(False)
