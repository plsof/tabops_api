from rest_framework import serializers

from ..models import Idc


class IdcSerializer(serializers.ModelSerializer):
    isp_name = serializers.SerializerMethodField()

    class Meta:
        model = Idc
        fields = ['id', 'name', 'address', 'isp', 'bandwidth', 'ip_range', 'comment', 'isp_name']

    def get_isp_name(self, obj):
        return obj.get_isp_display()
