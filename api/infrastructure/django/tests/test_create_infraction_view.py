import uuid
from datetime import datetime

from django.utils.timezone import make_aware
from rest_framework import status
from rest_framework.reverse import reverse

from api.domain.entities.infraction_entity import InfractionEntity
from api.infrastructure.django.models import Officer
from api.infrastructure.django.models.infraction import Infraction
from api.infrastructure.django.tests.test_set_up import TestSetUp


class TestCreateInfractionView(TestSetUp):
    def setUp(self):
        super().setUp()

        self._url_path = reverse("create-infraction-cargar-infraccion")
        self._data = {
            "placa_patente": "ABC123",
            "timestamp": "2024-07-01 12:35:55",
            "comentarios": "comments",
        }

        unique_id = str(uuid.uuid4())[:20]
        officer_data = {
            "name": "officer_1",
            "unique_id": unique_id,
        }
        Officer.objects.create(**officer_data)
        officer_token_url = reverse("token-officer-token")
        response = self.client.post(officer_token_url, data=officer_data, format="json")
        access_token = response.data["message"]["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    def test_create_infraction_unauthenticated(self):
        expected = status.HTTP_401_UNAUTHORIZED
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post(self._url_path, data=self._data, format="json")
        self.assertEqual(expected, response.status_code)

    def test_create_infraction_success(self):
        expected = {
            "message": {
                "comentarios": "comments",
                "placa_patente": "ABC123",
                "timestamp": "2024-07-01 12:35:55",
            }
        }

        response = self.client.post(self._url_path, data=self._data, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected, response.data)

    def test_create_infraction_success_data_in_db(self):
        datetime_naive = datetime(2024, 7, 1, 12, 35, 55)
        datetime_aware = make_aware(datetime_naive)
        expected = InfractionEntity(
            vehicle=self._vehicle_1.to_entity(),
            timestamp=datetime_aware,
            comments="comments",
        )

        response = self.client.post(self._url_path, data=self._data, format="json")
        infraction = Infraction.objects.get(
            vehicle__license_plate=expected.vehicle.license_plate
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected, infraction.to_entity())

    def test_create_infraction_missing_fields(self):
        expected = {
            "error": "Serializer error: {'placa_patente': [ErrorDetail(string='This field is required.', code='required')]}."
        }
        data = {**self._data}
        data.pop("placa_patente")
        response = self.client.post(self._url_path, data=data, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected, response.data)

    def test_create_infraction_field_not_exist(self):
        expected = {"error": "Vehicle does not exist."}
        data = {
            "placa_patente": "NotExist",
            "timestamp": "2024-07-01 12:35:55",
            "comentarios": "comments",
        }
        response = self.client.post(self._url_path, data=data, format="json")
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual(expected, response.data)

    def test_create_infraction_field_is_null(self):
        expected = {
            "error": "Serializer error: {'comentarios': [ErrorDetail(string='This field may not be null.', code='null')]}."
        }
        data = {
            "placa_patente": "NotExist",
            "timestamp": "2024-07-01 12:35:55",
            "comentarios": None,
        }
        response = self.client.post(self._url_path, data=data, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected, response.data)
