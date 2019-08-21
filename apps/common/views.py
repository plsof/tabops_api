from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


# 自定义分页
class MyPageNumber(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'limit'


# 自定义返回格式
class ResponseInfo(object):
    def __init__(self, **args):
        self.response = {
            "code": args.get('code', 0),
            "data": args.get('data', []),
            "msg": args.get('msg', 'success')
        }


class ResponseModelViewSet(ModelViewSet):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ResponseModelViewSet, self).__init__(**kwargs)

    def list(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).list(request, *args, **kwargs)
        page_obj = MyPageNumber()
        page_data = page_obj.paginate_queryset(queryset=response_data.data, request=request, view=self)
        # self.response_format["data"] = response_data.data
        self.response_format["data"] = page_data
        self.response_format["total"] = len(response_data.data)
        self.response_format["code"] = 0
        if not response_data.data:
            self.response_format["msg"] = "List empty"
        return Response(self.response_format)

    def create(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).create(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["code"] = 0
        return Response(self.response_format)

    def retrieve(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).retrieve(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["code"] = 0
        if not response_data.data:
            self.response_format["msg"] = "Empty"
        return Response(self.response_format)

    def update(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).update(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["code"] = 0
        return Response(self.response_format)

    def destroy(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).destroy(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["code"] = 0
        return Response(self.response_format)
