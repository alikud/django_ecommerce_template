from datetime import datetime, timedelta

# Create your models here.
import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
import uuid
from .services.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    email = models.EmailField(db_index=True, unique=True, max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return f"email: {self.email}"

    @property
    def token(self):
        return self.generate_jwt_token()

    def generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': str(self.pk),
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
