from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from common.views import ResponseInfo, MyPageNumber
from .models import File
from .serializers import FileSerializer


class FileUploadView(APIView):
    permission_classes = [IsAdminUser]

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(FileUploadView, self).__init__(**kwargs)

    def get(self, request, format=None):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        page = self.request.query_params.get('page', None)
        if page is not None and page is not '':
            page_obj = MyPageNumber()
            page_data = page_obj.paginate_queryset(queryset=serializer.data, request=request, view=self)
            self.response_format["data"] = page_data
        else:
            self.response_format["data"] = serializer.data
        self.response_format["total"] = len(serializer.data)
        self.response_format["code"] = 0
        if not serializer.data:
            self.response_format["msg"] = "List empty"
        return Response(self.response_format)

    def post(self, request, format=None):

        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDetailView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, pk, format=None):
        file = self.get_object(pk)
        file.file.delete()  # 物理删除图片
        file.delete()  # 删除数据库记录
        return Response(status=status.HTTP_204_NO_CONTENT)
