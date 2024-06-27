from django.db import models

from api.domain.entities.person_entity import PersonEntity


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        ordering = ["name"]

    def to_entity(self):
        return PersonEntity(
            name=self.name,
            email=self.email,
        )

    def __str__(self):
        return self.name
