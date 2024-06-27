from datetime import datetime

from rest_framework import status
from rest_framework.reverse import reverse

from api.infrastructure.django.models.infraction import Infraction
from api.infrastructure.django.tests.test_set_up import TestSetUp


class TestListInfractionView(TestSetUp):
    def setUp(self):
        super().setUp()
        self._data = {"email": "user@email.com"}
        self._url_path = reverse("list-infraction-generar-informe")

    def test_list_infraction_email_not_exist(self):
        expected = {"error": "Person does not exist."}
        data = {"email": "no@exist.com"}
        response = self.client.post(self._url_path, data=data, format="json")
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual(expected, response.data)

    def test_list_infraction_wrong_data(self):
        expected = {
            "error": "Serializer error: {'email': [ErrorDetail(string='This field is required.', code='required')]}."
        }
        data = {"wrong_data": "wrong_data"}
        response = self.client.post(self._url_path, data=data, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected, response.data)

    def test_list_infraction_invalid_email(self):
        expected = {
            "error": "Serializer error: {'email': [ErrorDetail(string='Enter a valid email address.', code='invalid')]}."
        }
        data = {"email": "wrong_data"}
        response = self.client.post(self._url_path, data=data, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected, response.data)

    def test_list_infraction_no_infraction(self):
        expected = {"message": "No registra infracciones"}
        data = {"email": "john@example.com"}
        response = self.client.post(self._url_path, data=data, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected, response.data)

    def test_list_infraction_exist_infractions(self):
        expected = {
            "message": [
                {
                    "comentarios": "Estacionamiento prohibido",
                    "placa_patente": "456QWE",
                    "timestamp": "2024-07-02 14:45:30",
                },
                {
                    "comentarios": "Exceso de velocidad",
                    "placa_patente": "ABC123",
                    "timestamp": "2024-07-01 12:35:55",
                },
            ]
        }
        data = {"email": "john@example.com"}
        Infraction.objects.create(
            vehicle=self._vehicle_1,
            timestamp=datetime(2024, 7, 1, 12, 35, 55),
            comments="Exceso de velocidad",
        )
        Infraction.objects.create(
            vehicle=self._vehicle_2,
            timestamp=datetime(2024, 7, 2, 14, 45, 30),
            comments="Estacionamiento prohibido",
        )
        Infraction.objects.create(
            vehicle=self._vehicle_3,
            timestamp=datetime(2024, 7, 3, 16, 50, 15),
            comments="Pasar semáforo en rojo",
        )
        response = self.client.post(self._url_path, data=data, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected, response.data)
