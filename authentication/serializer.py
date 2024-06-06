from rest_framework import serializers

from authentication.models import Admin, Instructor, Student


class RegisterAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # does the password get hashed automatically
        admin = Admin(
            username=validated_data["username"],
            is_superuser=True,
        )
        admin.set_password(validated_data["password"])
        admin.save()
        return admin


class RegisterInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ["username", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        instructor = Instructor(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_superuser=False,
        )
        instructor.set_password(validated_data["password"])
        instructor.save()
        return instructor


class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "student_id",
            "major",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        student = Student(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            student_id=validated_data["student_id"],
            major=validated_data["major"],
            is_superuser=False,
        )
        student.set_password(validated_data["password"])
        return student
