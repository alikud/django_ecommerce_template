import pytest
import requests
from django.db.utils import IntegrityError
from django.test import Client
from django.urls import get_resolver
from users.models import User
import json
from rest_framework.test import APIClient, APIRequestFactory
from users.views import LoginAPIView

pytestmark = [pytest.mark.django_db]

email = 'email_from_test@mail.com'
token = ''
password = 'ahjksdhklh123'

class TestUsers:
    def test_my_user(self, user):
        me: User = User.objects.get(email='somemail@gmail.com')
        assert me.token == user.token
        assert not me.is_superuser

    @pytest.mark.urls('users.urls')
    def test_something(self, client):
        assert 'Success!' in client.post('/login/').content

    @pytest.mark.urls('users.urls')
    def test_details(self, rf):
        request = rf.get('/login/')
        response = LoginAPIView(request)
        assert response.status_code == 200


# class TestUsers:
#     pytestmark = pytest.mark.django_db

#     def test_my_user(self):
#         me = User.objects.get(email='somemail@gmail.com')
#         assert me.is_superuser