from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    idc_name = serializers.SerializerMethodField()
    service_name = serializers.SerializerMethodField()
    z_status = serializers.SerializerMethodField()

    def get_idc_name(self, obj):
        return obj.idc.name

    def get_service_name(self, obj):
        return obj.service.name

    def get_z_status(self, obj):
        return obj.get_status_display()

    class Meta:
        fields = ['id', 'idc', 'idc_name', 'service', 'service_name', 'ip', 'path', 'port', 'status', 'z_status',
                  'comment']
        abstract = True
