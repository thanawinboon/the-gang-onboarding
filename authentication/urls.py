from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    AssignInstructorToStudentView,
    ListInstructorsView,
    ListStudentsView,
    RegisterAdminView,
    RegisterInstructorView,
    RegisterStudentView,
)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/admin", RegisterAdminView.as_view(), name="register_admin"),
    path(
        "register/instructor",
        RegisterInstructorView.as_view(),
        name="register_instructor",
    ),
    path("register/student", RegisterStudentView.as_view(), name="register_student"),
    path("instructor/list", ListInstructorsView.as_view(), name="list_student"),
    path("student/list", ListStudentsView.as_view(), name="list_student"),
    path(
        "instructor/assign",
        AssignInstructorToStudentView.as_view(),
        name="assign_instructor_to_student",
    ),
]
