from django.test import TestCase
from vms.models import StudentVehicle, FacultyVehicle , Guard, Gate, ParkingSlot, SuspiciousVehicle, ResidentLog, VisitorLog, TheftReport , VehiclePass, Route, Place, BusTiming , PersonPass, Day , Available
from datetime import datetime


class GateTestCase(TestCase):
	def setup(self):
		Gate.objects.create(gate_name = "Main gate" , security_on_duty="ram")
		Gate.objects.create(gate_name = "K.V. gate" , security_on_duty="shyam")
		Gate.objects.create(gate_name = "ASEB gate" , security_on_duty="Mohan")
		Gate.objects.create(gate_name = "Lathia Baghicha gate" , security_on_duty="sohan")

class GuardTestCase(TestCase):
	def setup(self):
		Guard.objects.create(guard_name = "ram")
		Guard.objects.create(guard_name = "shyam")
		Guard.objects.create(guard_name = "Mohan")
		Guard.objects.create(guard_name = "sohan")


# Create your tests here.
class ParkingSlotTestCase(TestCase):
	def setup(self):
		ParkingSlot.objects.create(total_slots = 30 , security_on_duty="ram" , parking_area_name = "Academic Complex" , available_slots = 12)
		ParkingSlot.objects.create(total_slots = 30 , security_on_duty="shyam" , parking_area_name = "Admin Building" , available_slots = 6)
		ParkingSlot.objects.create(total_slots = 30 , security_on_duty="Mohan" , parking_area_name = "Core 4" , available_slots = 3)
		ParkingSlot.objects.create(total_slots = 30 , security_on_duty="sohan" , parking_area_name = "Core 2" , available_slots = 1)


class ResidentLogTestCase(TestCase):
	def setup(self):
		ResidentLog.objects.create(registration_number = "3456" , vehicle_type ="car" , vehicle_model= "Hyundai Verna" , gate = "Main gate", is_entering = True)
		ResidentLog.objects.create(registration_number = "AS34" , vehicle_type ="bike" , vehicle_model = "Hero Honda" , gate = "Main gate" , is_entering = False)
		ResidentLog.objects.create(registration_number = "CV30" , vehicle_type ="bicycle" , vehicle_model = "Ladybird" , gate = "Main gate" , is_entering = True)
		ResidentLog.objects.create(registration_number = "3UI0" , vehicle_type ="other" , vehicle_model = "Tata Sumo" , gate = "Main gate" , is_entering = False)

class VisitorLogTestCase(TestCase):
	def setup(self):
		VisitorLog.objects.create(vehicle_number = "3456" , in_gate="Main gate",out_gate="Main gate",vehicle_type ="car" , vehicle_model= "Hyundai Verna" ,driver_name="raju",license_number="24255",place_to_visit="Subansiri",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S'))
		VisitorLog.objects.create(vehicle_number = "1256" , in_gate="ASEB gate",out_gate="Main gate",vehicle_type ="car" , vehicle_model= "Hyundai Verna" ,driver_name="raghu",license_number="23425",place_to_visit="kameng",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S'))
		VisitorLog.objects.create(vehicle_number = "8956" , in_gate="K.V. gate",out_gate="Main gate",vehicle_type ="auto" , vehicle_model= "Hyundai Verna" ,driver_name="raja",license_number="34255",place_to_visit="manas",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S'))
		VisitorLog.objects.create(vehicle_number = "3556" , in_gate="Main gate",out_gate="ASEB gate",vehicle_type ="bike" , vehicle_model= "Hyundai Verna" ,driver_name="manoj",license_number="24345",place_to_visit="kapili",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:00','%Y-%m-%d %H:%M:%S'))

class RouteTestCase(TestCase):
	def setup(self):
		Route.objects.create(place="PBWT-" , bus="B1")
		Route.objects.create(place="BHM-" , bus="B2")
		Route.objects.create(place="ADMN" , bus="B2")
		Route.objects.create(place="JG-" , bus="B1")


class PlaceTestCase(TestCase):
	def setup(self):
		Place.objects.create(place_name="PBWT-")
		Place.objects.create(place_name="BHM-")
		Place.objects.create(place_name="ADMN-")
		Place.objects.create(place_name="AG-")
		Place.objects.create(place_name="JG-")
		Place.objects.create(place_name="Com C-")

class VehiclePassTestCase(TestCase):
	def setup(self):
		VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="RJ-06 1111", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="bike")
		VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="AS-07 1231", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="car")
		VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="RJ-06 1141", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="bike")
		VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="AS-05 2341", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="auto")


class TheftReportTestCase(TestCase):
	def setup(self):	
		TheftReport.objects.create(registration_number="1234" , reporter="admin" ,vehicle_type="bike",  vehicle_model="d-24", theft_time=datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S'), theft_place="core1" , remarks="none" ,status="found" )
		TheftReport.objects.create(registration_number="5352" , reporter="admin" ,vehicle_type="bicycle",  vehicle_model="if-54", theft_time=datetime.strptime('2015-07-05 06:36:57','%Y-%m-%d %H:%M:%S'), theft_place="core2" , remarks="none" ,status="found" )
		TheftReport.objects.create(registration_number="4242" , reporter="admin" ,vehicle_type="car",  vehicle_model="asd", theft_time=datetime.strptime('2015-07-05 06:37:57','%Y-%m-%d %H:%M:%S'), theft_place="Admin" , remarks="none" ,status="not found" )
		TheftReport.objects.create(registration_number="4235" , reporter="admin" ,vehicle_type="auto",  vehicle_model="a3f", theft_time=datetime.strptime('2015-07-05 06:38:57','%Y-%m-%d %H:%M:%S'), theft_place="hostel" , remarks="none" ,status="not found" )