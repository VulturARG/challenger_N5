from rest_framework import serializers

from api.infrastructure.django.models import Officer


class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ["name", "unique_id"]
        extra_kwargs = {
            "unique_id": {"validators": []},
        }
