from django.urls import path

from .views import UserCreateAPIView


urlpatterns = [
    path(r'register/', UserCreateAPIView.as_view()),
]
