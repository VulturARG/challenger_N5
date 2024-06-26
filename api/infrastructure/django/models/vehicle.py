from django.db import models


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    person = models.ForeignKey(
        "Person", on_delete=models.CASCADE, related_name="vehicles"
    )

    def __str__(self):
        return self.license_plate
