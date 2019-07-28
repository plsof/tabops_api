from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BussinessList(ListCreateAPIView):
    queryset = Bussiness.objects.all()
    serializer_class = BussinessSerializer

    def get_queryset(self):
        queryset = Bussiness.objects.all()
        name = self.request.query_params.get('name', None)
        btype = self.request.query_params.get('btype', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        if btype is not None and btype is not '':
            queryset = queryset.filter(btype=btype)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BussinessAction(RetrieveUpdateDestroyAPIView):
    queryset = Bussiness.objects.all()
    serializer_class = BussinessSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ServiceList(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        bussiness = self.request.query_params.get('bussiness', None)
        if bussiness is not None and bussiness is not '':
            queryset = queryset.filter(bussiness=bussiness)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ServiceAction(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)