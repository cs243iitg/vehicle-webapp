from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from vms.models import TheftReport
from vms.models import SuspiciousVehicle
from vms.models import ParkingSlot
from rest.serializers import TheftReportSerializer
from rest.serializers import SuspiciousVehicleSerializer
from rest.serializers import ParkingSlotSerializer
from rest.permissions import IsReporter



# Test view
@api_view(['GET', 'POST'])
def test_view(request):
    data = {'hello': 'world'}
    return Response(data)

#list of theft reports
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def theft_report(request):
    if request.method == 'GET':
        theft_reports = TheftReport.objects.filter(reporter=request.user)
        serializer = TheftReportSerializer(theft_reports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TheftReportSerializer(data=request.data)
        if serializer.is_valid():
            #look for vehicle in the database
            vehicles = []
            if(request.user.is_student):
                vehicles = StudentVehicle.objects.filter(vehicle_registration_number=request.data.registration_number)
                if(len(vehicles)>0):
                    serializer.save(reporter=request.user, stud_vehicle=vehicles[0])
            elif(request.user.is_staff):
                vehicles = EmployeeVehicle.objects.filter(vehicle_registration_number=request.data.registration_number)
                if(len(vehicles)>0):
                    serializer.save(reporter=request.user, emp_vehicle=vehicles[0])
            else:
                serializer.save(reporter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#details of theft report
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsReporter,))
def theft_detail(request, pk):
    try:
        theft_report = TheftReport.objects.get(pk=pk)
    except TheftReport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TheftReportSerializer(theft_report)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TheftReportSerializer(theft_report, data=request.data)
        if serializer.is_valid():
            serializer.save(reporter=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        TheftReport.delete(theft_report)
        return Response(status=status.HTTP_204_NO_CONTENT)


#list of suspicious vehicles
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def suspicious_vehicle(request):
    if request.method == 'GET':
        suspicious_vehicles = SuspiciousVehicle.objects.filter(reporter=request.user)
        serializer = SuspiciousVehicleSerializer(suspicious_vehicles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuspiciousVehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(reporter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#list of parking slots
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def parking_slot(request):
    if request.method == 'GET':
        parking_slots = ParkingSlot.objects.all()
        serializer = ParkingSlotSerializer(parking_slots, many=True)
        return Response(serializer.data)
