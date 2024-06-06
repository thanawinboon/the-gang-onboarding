from models import Admin, Instructor, Student
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and isinstance(request.user, Admin)


class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return request.user and isinstance(request.user, Instructor)


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and isinstance(request.user, Student)
