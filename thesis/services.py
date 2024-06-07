import datetime
import os

from dotenv import load_dotenv
from models import Review, Thesis, UploadedFile

load_dotenv()
ACCESS_KEY = os.getenv("S3_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("S3_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


# assume that this could be thrown to a microservice to handle
def upload_file_to_s3(file_obj):
    file_name = "test_file.pdf"
    if file_obj:
        file_name = file_name + ".pdf"
    try:
        return f"https://{BUCKET_NAME}.s3.amazonaws.com/{file_name}"
    except Exception as e:
        print(e)
        return None


def register_uploaded_file(student, s3_url):
    date_today = datetime.date.today()
    expiry_date = date_today + datetime.timedelta(days=2)
    new_file = UploadedFile(uploader=student, s3_url=s3_url, expires=expiry_date)
    new_file.save()
    return new_file


def list_uploaded_files(student):
    queryset = UploadedFile.objects.filter(
        uploader=student, expires__gte=datetime.date.today()
    )
    return queryset


def submit_thesis(uploaded_file_id, thesis_title):
    uploaded_file = UploadedFile.objects.get(id=uploaded_file_id)
    thesis = Thesis(
        title=thesis_title,
        owner=uploaded_file.uploader,
        s3_url=uploaded_file.s3_url,
    )
    thesis.save()
    return thesis


def create_review(thesis_id, comments, is_approved):
    target_thesis = Thesis.objects.get(id=thesis_id)
    new_review = Review(
        thesis=target_thesis,
        comments=comments,
        is_approved=is_approved,
    )
    new_review.save()
    if is_approved:
        target_thesis.status = Thesis.ThesisStatus.APPROVED
    else:
        target_thesis.status = Thesis.ThesisStatus.REJECTED
    target_thesis.save()
    return new_review
