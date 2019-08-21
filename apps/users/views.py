from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from common.views import ResponseModelViewSet
from django.contrib.auth.models import User
from rest_framework import status

from .serializers import UserSerializer


class UserViewSet(ResponseModelViewSet):
    serializer_class = UserSerializer
    model = User

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None and username is not '':
            queryset = queryset.filter(username=username)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        self.perform_create(serializer)
        self.response_format["data"] = serializer.data
        self.response_format["code"] = 0
        headers = self.get_success_headers(serializer.data)
        return Response(self.response_format, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        self.perform_update(serializer)
        self.response_format["data"] = serializer.data
        self.response_format["code"] = 0
        headers = self.get_success_headers(serializer.data)
        return Response(self.response_format, status=status.HTTP_206_PARTIAL_CONTENT, headers=headers)
