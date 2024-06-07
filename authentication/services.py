from authentication.models import Instructor, Student


def list_students(request):
    major = request.GET.get("major")
    student_id = request.GET.get("student_id")
    first_name = request.GET.get("first_name")
    last_name = request.GET.get("last_name")

    queryset = Student.objects.all()
    if major:
        # assuming there is a dropdown on the Frontend
        queryset = queryset.filter(major=major)
    if student_id:
        queryset = queryset.filter(student_id__contains=student_id)
    if first_name:
        queryset = queryset.filter(first_name__contains=first_name)
    if last_name:
        queryset = queryset.filter(last_name__contains=last_name)
    return queryset


def list_instructors(request):
    first_name = request.GET.get("first_name")
    last_name = request.GET.get("last_name")

    queryset = Instructor.objects.all()
    if first_name:
        queryset = queryset.filter(first_name__contains=first_name)
    if last_name:
        queryset = queryset.filter(last_name__contains=last_name)
    return queryset


def assign_instructor_to_student(instructor_id, student_ids):
    instructor = Instructor.objects.get(id=instructor_id)
    Student.objects.filter(id__in=student_ids).update(instructor=instructor)
