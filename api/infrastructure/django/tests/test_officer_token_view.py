import uuid

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from api.infrastructure.django.models import Officer


class TestOfficerTokenView(APITestCase):
    def setUp(self):
        self._unique_id = str(uuid.uuid4())[:20]
        self._officer = Officer.objects.create(
            name="officer_1", unique_id=self._unique_id
        )
        self._url = reverse("token-officer-token")

    def test_get_valid_token(self):
        expected = status.HTTP_200_OK
        data = {
            "name": "officer_1",
            "unique_id": self._unique_id,
        }
        response = self.client.post(self._url, data=data, format="json")
        self.assertEqual(expected, response.status_code)
        self.assertIn("message", response.data)
        message = response.data["message"]
        self.assertIn("access", message)
        self.assertIn("refresh", message)

    def test_token_officer_not_in_db(self):
        expected_status = status.HTTP_404_NOT_FOUND
        expected_message = {"error": "Officer does not exist."}
        data = {
            "name": "officer_2",
            "unique_id": "1234",
        }
        response = self.client.post(self._url, data=data, format="json")
        self.assertEqual(expected_status, response.status_code)
        self.assertEqual(expected_message, response.data)
