# handlers
from django.urls import path

from .views import LoginAPIView, ProfileAPIView, RegistrationAPIView

app_name = 'users'
urlpatterns = [
    path('sign-up/', RegistrationAPIView.as_view()),
    path('sign-in/', LoginAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view())
]
