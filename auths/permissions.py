from rest_framework import permissions

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the 'teacher' group
        return request.user.groups.filter(name='teachers').exists()
    
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the 'teacher' group
        return request.user.groups.filter(name='student').exists()