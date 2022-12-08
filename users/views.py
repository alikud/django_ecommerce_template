from datetime import datetime

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.backends import JWTAuthentication

from .api.serializers import LoginSerializer, RegistrationSerializer

# from .renders import UserJSONRenderer


class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    # renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        # user = request.data.get('user', {})
        user = {"email": request.data.get('email'), "password": request.data.get('password')}

        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes =(AllowAny,)
    # authentication_classes =(JWTAuthentication, )
    serializer_class = LoginSerializer

    def post(self, request):
        user = {"email": request.data.get('email'), "password": request.data.get('password')}
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes =(JWTAuthentication, )
    # renderer_classes = (UserJSONRenderer,)
    def post(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return Response({"time": current_time}, status=status.HTTP_200_OK)
