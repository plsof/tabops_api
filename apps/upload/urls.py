from django.urls import path

from .views import FileUploadView, FileDetailView

urlpatterns = [
    path(r'', FileUploadView.as_view()),
    path(r'<int:pk>/', FileDetailView.as_view()),
]
