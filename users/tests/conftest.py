import pytest
from rest_framework.test import APIClient
from users.models import User

pytestmark = [pytest.mark.django_db]

@pytest.fixture
def user():
    return User.objects.create(email="somemail@gmail.com", password = "somepassword1234")

@pytest.fixture
def client() -> APIClient:
    return APIClient()
