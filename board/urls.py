from django.urls import path

from .views import TaskAPIView

app_name = 'board'
urlpatterns = [
    path('task/', TaskAPIView.as_view()),

]
