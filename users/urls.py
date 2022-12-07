# handlers
from django.urls import path

from .views import LoginAPIView, ProfileAPIView, RegistrationAPIView

app_name = 'users'
urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view())
]
