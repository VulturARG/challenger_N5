from rest_framework import serializers

from api.infrastructure.django.models.infraction import Infraction


class InfractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraction
        fields = ["vehicle", "timestamp", "comments"]
