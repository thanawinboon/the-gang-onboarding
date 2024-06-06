from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomBaseUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "admin", "Administrator"
        INSTRUCTOR = "instructor", "Instructor"
        STUDENT = "student", "Student"

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    first_name = None
    last_name = None
    email = None

    base_role = Roles.ADMIN
    roles = models.CharField(
        "Roles", max_length=20, choices=Roles.choices, default=Roles.ADMIN
    )


class Admin(CustomBaseUser):
    base_role = CustomBaseUser.Roles.ADMIN


class Instructor(CustomBaseUser):
    base_role = CustomBaseUser.Roles.INSTRUCTOR
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Student(CustomBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    major = models.CharField(max_length=50)

    advisor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)

    base_role = CustomBaseUser.Roles.STUDENT
