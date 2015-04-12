from django.test import TestCase
from vms.models import IITGUser, StudentVehicle, EmployeeVehicle , Guard, Gate, ParkingSlot, SuspiciousVehicle, ResidentLog, VisitorLog, TheftReport , VehiclePass, Place, BusTiming , PersonPass, Day
from datetime import datetime
from django.contrib.auth.models import User

g1=Guard.objects.create(guard_name = "ram", guard_phone_number="8011034051").save()
g2=Guard.objects.create(guard_name = "shyam", guard_phone_number="123").save()
g3=Guard.objects.create(guard_name = "Mohan", guard_phone_number="123").save()
g4=Guard.objects.create(guard_name = "sohan", guard_phone_number="123").save()

ga1=Gate.objects.create(gate_name = "Main gate" , security_on_duty=g1).save()
ga2=Gate.objects.create(gate_name = "K.V. gate" , security_on_duty=g2).save()
ga3=Gate.objects.create(gate_name = "ASEB gate" , security_on_duty=g3).save()
ga4=Gate.objects.create(gate_name = "Lathia Baghicha gate" , security_on_duty=g4).save()


ParkingSlot.objects.create(total_slots = 30 , security_on_duty=g1 , parking_area_name = "Academic Complex" , available_slots = 12).save()
ParkingSlot.objects.create(total_slots = 30 , security_on_duty=g2 , parking_area_name = "Admin Building" , available_slots = 6).save()
ParkingSlot.objects.create(total_slots = 30 , security_on_duty=g3 , parking_area_name = "Core 4" , available_slots = 3).save()
ParkingSlot.objects.create(total_slots = 30 , security_on_duty=g4 , parking_area_name = "Core 2" , available_slots = 1).save()

ResidentLog.objects.create(registration_number = "3456" , vehicle_type ="car" , vehicle_model= "Hyundai Verna" , gate = ga1, is_entering = True).save()
ResidentLog.objects.create(registration_number = "AS34" , vehicle_type ="bike" , vehicle_model = "Hero Honda" , gate = ga2 , is_entering = False).save()
ResidentLog.objects.create(registration_number = "CV30" , vehicle_type ="bicycle" , vehicle_model = "Ladybird" , gate = ga3 , is_entering = True).save()
ResidentLog.objects.create(registration_number = "3UI0" , vehicle_type ="other" , vehicle_model = "Tata Sumo" , gate = ga4 , is_entering = False).save()

VisitorLog.objects.create(vehicle_number = "3456" , in_gate=ga1,out_gate=ga4,vehicle_type ="car" , vehicle_model= "Hyundai Verna" ,driver_name="raju",license_number="24255",place_to_visit="Subansiri",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
VisitorLog.objects.create(vehicle_number = "1256" , in_gate=ga2,out_gate=ga1,vehicle_type ="car" , vehicle_model= "Hyundai Verna" ,driver_name="raghu",license_number="23425",place_to_visit="kameng",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
VisitorLog.objects.create(vehicle_number = "8956" , in_gate=ga3,out_gate=ga2,vehicle_type ="auto" , vehicle_model= "Hyundai Verna" ,driver_name="raja",license_number="34255",place_to_visit="manas",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
VisitorLog.objects.create(vehicle_number = "3556" , in_gate=ga4,out_gate=ga3,vehicle_type ="bike" , vehicle_model= "Hyundai Verna" ,driver_name="manoj",license_number="24345",place_to_visit="kapili",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:00','%Y-%m-%d %H:%M:%S')).save()

Place.objects.create(place_name="PBWT-").save()
Place.objects.create(place_name="BHM-").save()
Place.objects.create(place_name="ADMN-").save()
Place.objects.create(place_name="AG-").save()
Place.objects.create(place_name="JG-").save()
Place.objects.create(place_name="Com C-").save()

VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="RJ-06 1111", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="bike").save()
VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="AS-07 1231", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="car").save()
VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="RJ-06 1141", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="bike").save()
VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="AS-05 2341", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="auto").save()

TheftReport.objects.create(registration_number="1234" , reporter=User.objects.all()[0] ,vehicle_type="bike",  vehicle_model="d-24", theft_time=datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S'), theft_place="core1" , remarks="none" ,status="found" ).save()
TheftReport.objects.create(registration_number="5352" , reporter=User.objects.all()[0] ,vehicle_type="bicycle",  vehicle_model="if-54", theft_time=datetime.strptime('2015-07-05 06:36:57','%Y-%m-%d %H:%M:%S'), theft_place="core2" , remarks="none" ,status="found" ).save()
TheftReport.objects.create(registration_number="4242" , reporter=User.objects.all()[0] ,vehicle_type="car",  vehicle_model="asd", theft_time=datetime.strptime('2015-07-05 06:37:57','%Y-%m-%d %H:%M:%S'), theft_place="Admin" , remarks="none" ,status="not found" ).save()
TheftReport.objects.create(registration_number="4235" , reporter=User.objects.all()[0] ,vehicle_type="auto",  vehicle_model="a3f", theft_time=datetime.strptime('2015-07-05 06:38:57','%Y-%m-%d %H:%M:%S'), theft_place="hostel" , remarks="none" ,status="not found" ).save()