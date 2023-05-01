from rest_framework import serializers
from breeds.models import Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = (
            "id",
            "title",
            "breed_url",
            "image_path",
            "description",
            "published",
        )
