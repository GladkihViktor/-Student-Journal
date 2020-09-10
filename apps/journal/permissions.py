from rest_framework.permissions import BasePermission, SAFE_METHODS

TEACHER_METHODS = [
    'POST', 'PUT', 'PATCH', 'DELETE'
]


def validate_teachers_method(method: str, is_teacher: bool = False) -> bool:
    if method in SAFE_METHODS:
        return True
    if method in TEACHER_METHODS and is_teacher:
        return True
    return False


class TeacherPermission(BasePermission):
    """"""
    
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return validate_teachers_method(request.method, request.user.is_teacher)
    
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return validate_teachers_method(request.method, request.user.is_teacher)
