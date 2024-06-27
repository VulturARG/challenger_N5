from rest_framework import serializers

from api.infrastructure.django.models.infraction import Infraction


class InfractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraction
        fields = ["timestamp", "placa_patente", "comentarios"]

    placa_patente = serializers.CharField(source="vehicle.license_plate")
    timestamp = serializers.DateTimeField()
    comentarios = serializers.CharField()
