from rest_framework import serializers

from ..models import Wtv


class WtvSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField()
    zabbix_status = serializers.SerializerMethodField()

    class Meta:
        model = Wtv
        fields = ['idc', 'service', 'service_name', 'ip', 'path', 'port', 'status', 'zabbix_status', 'comment']

    def get_service_name(self, obj):
        return obj.service.name

    def get_zabbix_status(self, obj):
        return obj.get_status_display()
