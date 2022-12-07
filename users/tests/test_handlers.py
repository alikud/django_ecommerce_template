import pytest
from django.db.utils import IntegrityError
from users.models import User
import requests
from django.urls import get_resolver
from django.test import Client


pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize("handler_path,expected_code", [("registration", 403), ("login", 403), ("profile", 403)])
def test_check_health_handlers(handler_path, expected_code):
    c = Client()
    response = c.get(f"http://localhost:8000/api/users/{handler_path}/")
    assert response.status_code == expected_code

def test_some():
    print(get_resolver().reverse_dict.keys())