from rest_framework import serializers

from ..models import Wtv


class WtvSerializer(serializers.ModelSerializer):
    idc_name = serializers.SerializerMethodField()
    service_name = serializers.SerializerMethodField()
    zabbix_status = serializers.SerializerMethodField()

    class Meta:
        model = Wtv
        fields = ['id', 'idc', 'idc_name', 'service', 'service_name', 'ip', 'path', 'port', 'status', 'zabbix_status', 'comment']

    def get_idc_name(self, obj):
        return obj.idc.name

    def get_service_name(self, obj):
        return obj.service.name

    def get_zabbix_status(self, obj):
        return obj.get_status_display()
