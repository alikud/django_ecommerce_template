import pytest
import requests
from django.db.utils import IntegrityError
from django.test import Client
from django.urls import get_resolver
from users.models import User
import json
from rest_framework.test import RequestsClient
pytestmark = [pytest.mark.django_db]

# TODO Write tests to handlers
def test_check_health_handlers():
    client = RequestsClient()

    body = {"email":"someemail10@gmail.com", "password": "qwoeijzlkxcjl123"}
    # response = clieclient.post(f"http://localhost:8000/api/users/login/", data=body, content_type="application/json")
    # assert response.status_code == 200

def test_some():
    print(get_resolver().reverse_dict.keys())
