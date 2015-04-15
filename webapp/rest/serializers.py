from rest_framework import serializers
from vms.models import *

class TheftReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheftReport
        fields = ('id', 'vehicle_pass_no', 'theft_time', 'theft_place', 'remarks', 'status')

class SuspiciousVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspiciousVehicle
        fields = ('id', 'vehicle_number', 'vehicle_type', 'vehicle_model', 'remarks', 'vehicle_image')
class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ('parking_area_name', 'total_slots','available_slots')

class BusTimingSerializer(serializers.ModelSerializer):
    starting_point = serializers.SlugRelatedField(
        read_only=True,
        slug_field='place_name'
     )
    ending_point = serializers.SlugRelatedField(
        read_only=True,
        slug_field='place_name'
     )

    class Meta:
        model = BusTiming
        fields = ('from_time', 'starting_point', 'ending_point')

