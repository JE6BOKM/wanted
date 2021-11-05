import pytest
from rest_framework import status
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_register(
        self,
        no_auth_client,
        login_resp_schema,
    ):
        payload = {
            "username": "guest10",
            "email": "guest10@guest.com",
            "password1": "rkskekfkakqktk",
            "password2": "rkskekfkakqktk",
        }

        register_url = reverse("rest_register")

        # Test signup success
        resp = no_auth_client.post(register_url, data=payload, format="json")
        assert resp.status_code == status.HTTP_201_CREATED
        assert login_resp_schema.is_valid(resp.json())

    def test_login(
        self,
        no_auth_client,
        login_resp_schema,
        user,
    ):
        payload = {
            "email": "test-user@test.com",
            "password": "1234",
        }

        register_url = reverse("rest_login")

        # Test login success
        resp = no_auth_client.post(register_url, data=payload, format="json")
        assert resp.status_code == status.HTTP_200_OK
        assert login_resp_schema.is_valid(resp.json())
