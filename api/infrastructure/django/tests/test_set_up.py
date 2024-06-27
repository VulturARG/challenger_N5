from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from api.infrastructure.django.models import Person, Vehicle


class TestSetUp(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass", email="user@email.com"
        )
        self._person_1 = Person.objects.create(
            name="John Doe", email="john@example.com"
        )
        self._person_2 = Person.objects.create(
            name="Jane Doe", email="jane@example.com"
        )
        self._vehicle_1 = Vehicle.objects.create(
            license_plate="ABC123", brand="Brand 1", color="Blue", person=self._person_1
        )
        self._vehicle_2 = Vehicle.objects.create(
            license_plate="456QWE", brand="Brand 2", color="Blue", person=self._person_1
        )
        self._vehicle_3 = Vehicle.objects.create(
            license_plate="123ABC", brand="Brand 2", color="Blue", person=self._person_2
        )
