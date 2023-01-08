import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError
from rest_framework import authentication, exceptions
from rest_framework.request import Request

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: Request):
        """
        return (user, token) or raise Exception if auth. failed
        """
        try:
            token = request.headers['Authorization'].split(" ")
            payload = jwt.decode(token[1], settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload['id'])
            return user, payload['id']

        except ExpiredSignatureError:
            # token can be invalid, np. expired
            raise exceptions.AuthenticationFailed("Invalid token")
        except KeyError:
            # we don't have Authorization in Headers key or don't have token -> return None
            raise exceptions.AuthenticationFailed("Authorization error")
