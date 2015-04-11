from rest_framework import serializers
from vms.models import *

class TheftReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheftReport
        fields = ('id', 'registration_number', 'vehicle_type', 'vehicle_model', 'theft_time', 'theft_place', 'remarks')

class SuspiciousVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspiciousVehicle
        fields = ('id', 'vehicle_number', 'vehicle_type', 'vehicle_model', 'remarks')