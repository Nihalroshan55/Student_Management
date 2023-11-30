from rest_framework import permissions

class IsTeacherOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return  (user.user_type == 'teacher' or user.is_superuser)
    
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the 'student' group
        return request.user.groups.filter(name='student').exists() or IsTeacherOrAdmin()