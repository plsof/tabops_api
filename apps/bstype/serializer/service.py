from rest_framework import serializers

from bstype.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    # bussiness = serializers.CharField(source='bussiness.name')
    bussiness_name = serializers.SerializerMethodField()

    class Meta:
        model = Service
        # fields = '__all__'
        fields = ['id', 'create_time', 'update_time', 'name', 'comment', 'bussiness', 'bussiness_name']

    def get_bussiness_name(self, obj):
        return obj.bussiness.name
