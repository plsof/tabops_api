from rest_framework import serializers

from bstype.models import Bussiness


class BussinessSerializer(serializers.ModelSerializer):
    btype_name = serializers.SerializerMethodField()

    class Meta:
        model = Bussiness
        fields = ['id', 'name', 'btype', 'domain', 'comment', 'btype_name']

    def get_btype_name(self, obj):
        return obj.get_btype_display()
