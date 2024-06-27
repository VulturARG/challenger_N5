from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from api.infrastructure.django.tests.test_set_up import TestSetUp


class TestCreateInfractionView(TestSetUp):
    def setUp(self):
        super().setUp()

        self._url_path = reverse("create-infraction-cargar-infraccion")
        self._data = {
            "placa_patente": "ABC123",
            "timestamp": "2024-07-01 12:35:55",
            "comentarios": "hjsklhjfslkjf",
        }
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_create_infraction_unauthenticated(self):
        expected = status.HTTP_401_UNAUTHORIZED
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post(self._url_path, data=self._data, format="json")
        self.assertEqual(expected, response.status_code)

    def test_create_infraction_success(self):
        expected = {
            "message": {
                "comentarios": "hjsklhjfslkjf",
                "placa_patente": "ABC123",
                "timestamp": "2024-07-01 12:35:55",
            }
        }
        response = self.client.post(self._url_path, data=self._data, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected, response.data)

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
            "comentarios": "hjsklhjfslkjf",
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
