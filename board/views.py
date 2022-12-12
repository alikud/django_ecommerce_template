from datetime import datetime

from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.backends import JWTAuthentication
from users.models import User

from .models import Category, Subsciber, Tags, Task

# from users.backends import JWTAuthentication

# from .api.serializers import LoginSerializer, RegistrationSerializer

class TaskAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    # Some CRUD
    def post(self, request):
        user = request.user.objects.get(pk=request.auth)
        print(user.email)
        print(request.body.decode())
        #print(User.objects.all())
        # user: User = User.objects.get(id=request.user.id)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return Response({"post": current_time}, status=status.HTTP_200_OK)


    def get(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return Response({"get": current_time}, status=status.HTTP_200_OK)


    def patch(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return Response({"patch": current_time}, status=status.HTTP_200_OK)


    def delete(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return Response({"delete": current_time}, status=status.HTTP_200_OK)
