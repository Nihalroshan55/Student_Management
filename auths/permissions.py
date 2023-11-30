from rest_framework import permissions


# Custom permissions for authorisation

class IsTeacherOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        # returning True if the requested user.user_type is teacher or the user is superuser
        return  (user.user_type == 'teacher' or user.is_superuser)
    
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the 'student' or the user IsTeacherOrAdmin 
        return request.user.groups.filter(name='student').exists() or IsTeacherOrAdmin()