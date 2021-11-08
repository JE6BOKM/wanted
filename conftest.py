from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

import pytest
from dj_rest_auth.utils import jwt_encode
from rest_framework.test import APIClient

from test.factories import UserFactory

pytest_plugins = ["test.schema", "test.factories"]
pytestmark = pytest.mark.django_db

User = settings.AUTH_USER_MODEL


@pytest.fixture
def user() -> User:
    user = UserFactory(
        username="test-user",
        email="test-user@test.com",
        password="1234",
    )
    return user


@pytest.fixture
def client(user):
    access, __ = jwt_encode(user)  # access, refresh
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access}"}
    client = APIClient()
    client.credentials(**headers)
    return client


@pytest.fixture
def no_auth_client():
    client = APIClient()
    return client


@pytest.fixture
def fake_request(rf: RequestFactory, user):
    # build "request" for the test: needed to populate HiddenField(default=serializers.CreateUserDefault())
    request = rf.get("/fake-url/")
    # Django Test Case Error 'WSGIRequest' object has no attribute 'session'
    # https://stackoverflow.com/questions/35659676/django-test-case-error-wsgirequest-object-has-no-attribute-session
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    request.user = user
    return request
