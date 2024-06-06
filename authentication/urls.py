import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/admin", views.RegisterAdminView.as_view(), name="register_admin"),
    path(
        "register/instructor",
        views.RegisterInstructorView.as_view(),
        name="register_instructor",
    ),
    path(
        "register/student", views.RegisterStudentView.as_view(), name="register_student"
    ),
]
