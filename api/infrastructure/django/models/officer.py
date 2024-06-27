from django.db import models


class Officer(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Officer"
        verbose_name_plural = "Officers"
        ordering = ["name"]

    def __str__(self):
        return self.name
