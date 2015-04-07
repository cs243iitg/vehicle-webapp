from rest_framework import serializers
from vms.models import TheftReport

class TheftReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheftReport
        fields = ('id', 'reporter_name', 'registration_number', 'vehicle_type', 'vehicle_model', 'theft_time', 'theft_place', 'remarks')
