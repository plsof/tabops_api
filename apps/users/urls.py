from django.urls import path

from .views import UserList
from .views import UserDetail
from .views import UserCreateAPIView


urlpatterns = [
    path('', UserList.as_view()),
    path(r'<int:pk>/', UserDetail.as_view()),
    path(r'register/', UserCreateAPIView.as_view()),
]
