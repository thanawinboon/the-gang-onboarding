from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import Admin, Instructor, Student
from authentication.serializer import (
    InstructorSerializer,
    RegisterAdminSerializer,
    RegisterInstructorSerializer,
    RegisterStudentSerializer,
    StudentSerializer,
)
from authentication.services import (
    assign_instructor_to_student,
    list_instructors,
    list_students,
)


class RegisterAdminView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterAdminSerializer


class RegisterInstructorView(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterInstructorSerializer


class RegisterStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterStudentSerializer


class ListInstructorsView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = list_instructors(request)
        serializer = InstructorSerializer(queryset, many=True)
        return Response(serializer.data)


class ListStudentsView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = list_students(request)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)


class AssignInstructorToStudentView(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        instructor_id = request_data.get("instructor_id")
        student_ids = request_data.get("student_ids")
        assign_instructor_to_student(instructor_id, student_ids)
        return Response({"instructor_id": instructor_id, "student_ids": student_ids})
