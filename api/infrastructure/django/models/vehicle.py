from django.db import models

from api.domain.entities.vehicle_entity import VehicleEntity


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    person = models.ForeignKey(
        "Person", on_delete=models.CASCADE, related_name="vehicles"
    )

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehículos"
        ordering = ["license_plate"]

    def to_entity(self) -> VehicleEntity:
        return VehicleEntity(
            license_plate=self.license_plate,
            brand=self.brand,
            color=self.color,
            person=self.person.to_entity(),
        )

    def __str__(self):
        return self.license_plate
