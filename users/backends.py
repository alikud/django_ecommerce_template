from tkinter import E

import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError
from rest_framework import authentication, exceptions
from rest_framework.request import Request

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: Request):
        """
        Метод authenticate вызывается каждый раз, независимо от того, требует
        ли того эндпоинт аутентификации. 'authenticate' имеет два возможных
        возвращаемых значения:
            1) None - мы возвращаем None если не хотим аутентифицироваться.
            Обычно это означает, что мы значем, что аутентификация не удастся.
            Примером этого является, например, случай, когда токен не включен в
            заголовок.
            2) (user, token) - мы возвращаем комбинацию пользователь/токен
            тогда, когда аутентификация пройдена успешно. Если ни один из
            случаев не соблюден, это означает, что произошла ошибка, и мы
            ничего не возвращаем. В таком случае мы просто вызовем исключение
            AuthenticationFailed и позволим DRF сделать все остальное.
        """
        print('CALL AUTHENTICATE!')
        try:
            token = request.headers['Authorization']
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                # id extp
                user = User.objects.get(pk=payload['id'])
                return User, payload['id']
            except ExpiredSignatureError:
                print("faile to decode token")
            # print(payload)
        except KeyError:
            # we dont have Authorization in Headers key and dont have token -> return None
            raise exceptions.AuthenticationFailed("Authorization error")
            return None
