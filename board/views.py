from datetime import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from models import Task, Category, Tags, Subsciber
from users.backends import JWTAuthentication

from rest_framework import permissions
# from users.backends import JWTAuthentication

# from .api.serializers import LoginSerializer, RegistrationSerializer

class TaskAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # CRUD
    def post(self, request):
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