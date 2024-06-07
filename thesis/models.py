from django.db import models

from authentication.models import Student


class Thesis(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    class ThesisStatus(models.TextChoices):
        APPROVAL_PENDING = "APPROVAL_PENDING", "Approval Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    status = models.CharField(
        ThesisStatus, default=ThesisStatus.APPROVAL_PENDING, max_length=50
    )

    date_submitted = models.DateField(auto_now_add=True)
    s3_url = models.URLField()


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    comments = models.TextField()
    is_approved = models.BooleanField(default=False)


class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    uploader = models.ForeignKey(Student, on_delete=models.CASCADE)
    s3_url = models.URLField()

    # in case we can use a scheduler to remove the file after it expires
    expires = models.DateTimeField()
