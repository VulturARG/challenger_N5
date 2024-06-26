from django.db import models


class Officer(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
