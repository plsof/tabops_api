from rest_framework import serializers

from ..models import Host


class HostSerializer(serializers.ModelSerializer):
    # idc_name = serializers.SerializerMethodField()
    zabbix_status = serializers.SerializerMethodField()
    minion_status = serializers.SerializerMethodField()

    # def get_idc_name(self, obj):
    #     return obj.idc.name

    def get_zabbix_status(self, obj):
        return obj.get_z_status_display()

    def get_minion_status(self, obj):
        return obj.get_m_status_display()

    class Meta:
        model = Host
        fields = ['id', 'idc', 'salt_id', 'lan_ip', 'man_ip', 'platform', 'hostname', 'salt_version',
                  'os_finger', 'serial_number', 'mem_total', 'num_cpus', 'z_status', 'zabbix_status', 'm_status',
                  'minion_status', 'roles', 'comment']
