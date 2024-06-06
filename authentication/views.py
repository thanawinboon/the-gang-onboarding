from rest_framework import generics

from authentication.models import Admin, Instructor, Student
from authentication.serializer import (
    RegisterAdminSerializer,
    RegisterInstructorSerializer,
    RegisterStudentSerializer,
)

# from rest_framework.permissions import IsAdminUser


class RegisterAdminView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    # permission_classes = (IsAdminUser,)
    serializer_class = RegisterAdminSerializer


class RegisterInstructorView(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    # permission_classes = (IsAdminUser,)
    serializer_class = RegisterInstructorSerializer


class RegisterStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    # permission_classes = (IsAdminUser,)
    serializer_class = RegisterStudentSerializer
