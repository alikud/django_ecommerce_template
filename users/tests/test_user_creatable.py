import pytest
from django.db.utils import IntegrityError
from users.models import User

pytestmark = [pytest.mark.django_db]

def test_create_user(user):
    assert User.objects.get(email="somemail@gmail.com") == user

def test_two_users_with_same_email(user):
    with pytest.raises(IntegrityError):
        User.objects.create(email = user.email, password = "qwqjkoehgqwkje")




