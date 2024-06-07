from models import Review
from rest_framework import serializers


class CreateReviewSerializer(serializers.ModelSerializer):
    thesis_id = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ["comments", "is_approved"]
