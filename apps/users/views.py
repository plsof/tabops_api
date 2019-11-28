from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from common.views import ResponseModelViewSet
from django.contrib.auth.models import User
from rest_framework import status
from django.http import Http404
from rest_framework.generics import UpdateAPIView

from users import serializers


class UserViewSet(ResponseModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        username = self.request.query_params.get('username', None)
        if username is not None and username is not '':
            queryset = queryset.filter(username=username)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 明文密码加密
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
        # 明文密码加密
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        self.perform_update(serializer)
        self.response_format["data"] = serializer.data
        self.response_format["code"] = 0
        headers = self.get_success_headers(serializer.data)
        return Response(self.response_format, status=status.HTTP_206_PARTIAL_CONTENT, headers=headers)


class ChangePasswordView(UpdateAPIView):

    serializer_class = serializers.ChangePasswordSerializer
    # model = User

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = self.get_object(serializer.data.get("username"))
            # Check old password
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"msg": "旧密码错误"}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            newpass = serializer.data.get("new_password")
            if len(newpass) < 8:
                return Response({"msg": "新密码长度小于8"}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"msg": "密码更新成功"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
