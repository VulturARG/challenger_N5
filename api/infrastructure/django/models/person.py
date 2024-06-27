from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        ordering = ["name"]

    def __str__(self):
        return self.name
