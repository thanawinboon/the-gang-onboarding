from forms import UploadFileForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import CreateReviewSerializer
from services import (
    create_review,
    list_uploaded_files,
    register_uploaded_file,
    submit_thesis,
    upload_file_to_s3,
)

from authentication.permissions import IsInstructor, IsStudent


# https://github.com/axelpale/minimal-django-file-upload-example/blob/master/src/for_django_3-0/myapp/views.py
class UploadThesisView(APIView):
    permission_classes = (IsStudent,)

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if not form.is_valid():
            return

        file_obj = request.FILES["file"]
        file_url = upload_file_to_s3(file_obj)
        if not file_url:
            return Response(
                {"error": "Unable to upload file"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return register_uploaded_file(request.user, file_url)


class ListUploadedFileView(APIView):
    permission_classes = (IsStudent,)

    def get(self, request):
        return list_uploaded_files(request.user)


class SubmitThesisView(APIView):
    permission_classes = (IsStudent,)

    def post(self, request):
        uploaded_file_id = request.data.get("file_id")
        thesis_title = request.data.get("title")
        if not uploaded_file_id or not thesis_title:
            return Response(
                {"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST
            )
        thesis = submit_thesis(uploaded_file_id, thesis_title)
        return thesis


class ReviewThesisView(APIView):
    permission_classes = (IsInstructor,)

    def post(self, request):
        serializer = CreateReviewSerializer(request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        thesis_id = serializer.validated_data.get("thesis_id")
        comment = serializer.validated_data.get("comments")
        is_approved = serializer.validated_data.get("is_approved")

        review = create_review(thesis_id, comment, is_approved)
        return review
