from django.db import models

from api.domain.entities.infraction_entity import InfractionEntity


class Infraction(models.Model):
    vehicle = models.ForeignKey(
        "Vehicle", on_delete=models.CASCADE, related_name="infractions"
    )
    timestamp = models.DateTimeField()
    comments = models.TextField()

    class Meta:
        verbose_name = "Infracción"
        verbose_name_plural = "Infracciones"
        ordering = ["vehicle"]

    def to_entity(self):
        return InfractionEntity(
            vehicle=self.vehicle.to_entity(),
            timestamp=self.timestamp,
            comments=self.comments,
        )

    def __str__(self):
        return f"{self.vehicle.license_plate} - {self.timestamp}"
