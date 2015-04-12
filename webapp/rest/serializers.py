from rest_framework import serializers
from vms.models import *

class TheftReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheftReport
        fields = ('id', 'registration_number', 'theft_time', 'theft_place', 'remarks', 'status')

class SuspiciousVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspiciousVehicle
        fields = ('id', 'vehicle_number', 'vehicle_type', 'vehicle_model', 'remarks')
class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ('parking_area_name', 'total_slots','available_slots')