from django.test import TestCase
from vms.models import IITGUser, StudentVehicle, EmployeeVehicle , Guard, Gate, ParkingSlot, SuspiciousVehicle, ResidentLog, VisitorLog, TheftReport , Place, BusTiming , PersonPass, Day, OnDutyGuard
from datetime import datetime
from django.contrib.auth.models import User


"""
IITGUser TestCase

"""

try:
	u1=IITGUser.objects.create(user=User.objects.create_user(username="sumeet",password="sumeet"),is_student=True).save()
except Exception as e:
	print ("user not formed "+ str(e))

try:
	u2=IITGUser.objects.create(user=User.objects.create_superuser(username="admin",password="admin",email="admin@admin.com"),is_student=False).save()
except Exception as e:
	print ("admin not formed "+ str(e))

try:
	u3=IITGUser.objects.create(user=User.objects.create_user(username="abhi",password="abhi"),is_student=True).save()
except Exception as e:
	print ("user not formed "+ str(e))

try:
	u4=IITGUser.objects.create(user=User.objects.create_user(username="eeshani",password="eeshani"),is_student=True).save()
except Exception as e:
	print ("user not formed "+ str(e))


"""
StudentCycle TestCase

"""

try:
	sc1=StudentCycle.objects.create(cycle_user=User.objects.create_user(username="sumeet",password="sumeet"), cycle_model="hero", cycle_color="red", cycle_pass_no="7890", hostel="manas", room_number="B-234").save()
except Exception as e:
	print ("StudentCycle not formed "+ str(e))

try:
	sc2=StudentCycle.objects.create(cycle_user=User.objects.create_user(username="abhi",password="abhi"), cycle_model="ladybird", cycle_color="red", cycle_pass_no="7800", hostel="subansiri", room_number="D-119").save()
except Exception as e:
	print ("StudentCycle not formed "+ str(e))

try:
	sc2=StudentCycle.objects.create(cycle_user=User.objects.create_user(username="eeshani",password="eeshani"), cycle_model="terminator", cycle_color="white", cycle_pass_no="7834", hostel="subansiri", room_number="D-116").save()
except Exception as e:
	print ("StudentCycle not formed "+ str(e))



"""
Guard TestCase
"""
try:
	g1=Guard.objects.create(guard_user=User.objects.create_user(username="g1",password="g1"),guard_phone_number="8011034051", is_security=True).save()
except Exception as e:
	print ("Guard not formed "+ str(e))	

try:
	g2=Guard.objects.create(guard_user=User.objects.create_user(username="g2",password="g2"),guard_phone_number="8011034021", is_security=True).save()
except Exception as e:
	print ("Guard not formed "+ str(e))	

try:
	g3=Guard.objects.create(guard_user=User.objects.create_user(username="g3",password="g3"),guard_phone_number="8011034761", is_security=True).save()
except Exception as e:
	print ("Guard not formed "+ str(e))			


"""
OnDutyGuard TestCase

"""

try:
	o1=OnDutyGuard.objects.create(guard = g1 , place = "kv gate" , is_gate = True).save()
except Exception as e:
	print ("OnDutyGuard not formed "+ str(e))

try:
	o2=OnDutyGuard.objects.create(guard = g2 , place = "main gate" , is_gate = True).save()
except Exception as e:
	print ("OnDutyGuard not formed "+ str(e))

try:
	o2=OnDutyGuard.objects.create(guard = g3 , place = "Admn" , is_gate = False).save()
except Exception as e:
	print ("OnDutyGuard not formed "+ str(e))


"""
Gate TestCase

"""
try:
	gt1=Gate.objects.create(gate_name="Main gate").save()
except Exception as e:
	print ("gate not formed"+ str(e))

try:
	gt2=Gate.objects.create(gate_name="K.V. gate").save()
except Exception as e:
	print ("gate not formed"+ str(e))

try:
	gt3=Gate.objects.create(gate_name="ASEB gate").save()
except Exception as e:
	print ("gate not formed"+ str(e))

try:
	gt4=Gate.objects.create(gate_name="Lathia Baghicha gate").save()
except Exception as e:
	print ("gate not formed"+ str(e))



"""
ParkingSlot TestCase

"""

try:
	ps1=ParkingSlot.objects.create(total_slots = 30 , parking_area_name = "Academic Complex" , available_slots = 12).save()
except Exception as e:
	print ("ParkingSlot not formed "+ str(e))

try:
	ps2=ParkingSlot.objects.create(total_slots = 30 , parking_area_name = "Admin Building" , available_slots = 6).save()
except Exception as e:
	print ("ParkingSlot not formed "+ str(e))

try:
	ps3=ParkingSlot.objects.create(total_slots = 30 , parking_area_name = "Core 4" , available_slots = 3).save()
except Exception as e:
	print ("ParkingSlot not formed "+ str(e))

try:
	ps4=ParkingSlot.objects.create(total_slots = 30 , parking_area_name = "Core 2" , available_slots = 1).save()
except Exception as e:
	print ("ParkingSlot not formed "+ str(e))	


"""
ResidentLog TestCase

"""

try:
	r1=ResidentLog.objects.create(vehicle_pass_no= "3456" , in_time=datetime.strptime('2015-07-09 06:36:57','%Y-%m-%d %H:%M:%S'), out_time=datetime.strptime('2015-07-09 04:50:57','%Y-%m-%d %H:%M:%S'), in_gate = Gate.objects.all()[0], out_gate = Gate.objects.all()[3]).save()
except Exception as e:
	print ("ResidentLog not formed "+ str(e))

try:
	r2=ResidentLog.objects.create(vehicle_pass_no= "AS34" , in_time=datetime.strptime('2015-07-05 07:36:57','%Y-%m-%d %H:%M:%S'), out_time=datetime.strptime('2015-07-05 02:36:57','%Y-%m-%d %H:%M:%S'), in_gate = Gate.objects.all()[1] , out_gate = Gate.objects.all()[2]).save()
except Exception as e:
	print ("ResidentLog not formed "+ str(e))

try:
	r3=ResidentLog.objects.create(vehicle_pass_no= "CV30" , in_time=datetime.strptime('2015-02-05 09:36:57','%Y-%m-%d %H:%M:%S'), out_time=datetime.strptime('2015-02-05 05:36:57','%Y-%m-%d %H:%M:%S'), in_gate = Gate.objects.all()[2] , out_gate = Gate.objects.all()[2]).save()
except Exception as e:
	print ("ResidentLog not formed "+ str(e))

try:
	r4=ResidentLog.objects.create(vehicle_pass_no= "3UI0" , in_time=datetime.strptime('2015-06-05 10:36:57','%Y-%m-%d %H:%M:%S'), out_time=datetime.strptime('2015-06-05 06:36:57','%Y-%m-%d %H:%M:%S'), in_gate = Gate.objects.all()[3] , out_gate = Gate.objects.all()[0]).save()
except Exception as e:
	print ("ResidentLog not formed "+ str(e))



"""
VisitorLog TestCase

"""

try:
	v1=VisitorLog.objects.create(vehicle_number = "3456" , in_gate=Gate.objects.all()[0] , out_gate=Gate.objects.all()[0] , vehicle_type ="car" , vehicle_model= "Hyundai Verna" , driver_name="raju", license_number="24255", place_to_visit="Subansiri", purpose_of_visit="cab", in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
except Exception as e:
	print ("VisitorLog not formed "+ str(e))

try:
	v2=VisitorLog.objects.create(vehicle_number = "1256" , in_gate=Gate.objects.all()[1] , out_gate=Gate.objects.all()[1] , vehicle_type ="car" , vehicle_model= "Hyundai Verna" , driver_name="raghu", license_number="23425", place_to_visit="kameng", purpose_of_visit="cab", in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
except Exception as e:
	print ("VisitorLog not formed "+ str(e))

try:
	v3=VisitorLog.objects.create(vehicle_number = "8956" , in_gate=Gate.objects.all()[3] , out_gate=Gate.objects.all()[2] , vehicle_type ="auto" , vehicle_model= "Hyundai Verna" , driver_name="raja", license_number="34255", place_to_visit="manas", purpose_of_visit="cab", in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
except Exception as e:
	print ("VisitorLog not formed "+ str(e))

try:
	v4=VisitorLog.objects.create(vehicle_number = "3556" , in_gate=Gate.objects.all()[2] , out_gate=Gate.objects.all()[3] , vehicle_type ="bike" , vehicle_model= "Hyundai Verna" , driver_name="manoj", license_number="24345", place_to_visit="kapili", purpose_of_visit="cab", in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:00','%Y-%m-%d %H:%M:%S')).save()
except Exception as e:
	print ("VisitorLog not formed "+ str(e))



"""
Place TestCase

"""
try:
	p1=Place.objects.create(place_name="PBWT-").save()
except Exception as e:
	print ("place not formed"+ str(e))

try:
	p2=Place.objects.create(place_name="BHM-").save()
except Exception as e:
	print ("place not formed"+ str(e))

try:
	p3=Place.objects.create(place_name="ADMN-").save()
except Exception as e:
	print ("place not formed"+ str(e))

try:
	p4=Place.objects.create(place_name="AG-").save()
except Exception as e:
	print ("place not formed"+ str(e))

try:
	p5=Place.objects.create(place_name="JG-").save()
except Exception as e:
	print ("place not formed"+ str(e))

try:
	p6=Place.objects.create(place_name="Com C-").save()
except Exception as e:
	print ("place not formed"+ str(e))	


"""
Day TestCase

"""
try:
	d1=Day.objects.create(day="Monday").save()
except Exception as e:
	print ("day not formed"+ str(e))

try:
	d2=Day.objects.create(day="Tuesday").save()
except Exception as e:
	print ("day not formed"+ str(e))

try:
	d3=Day.objects.create(day="Wednesday").save()
except Exception as e:
	print ("day not formed"+ str(e))

try:
	d4=Day.objects.create(day="Thursday").save()
except Exception as e:
	print ("day not formed"+ str(e))

try:
	d5=Day.objects.create(day="Friday").save()
except Exception as e:
	print ("day not formed"+ str(e))

try:
	d6=Day.objects.create(day="Saturday").save()
except Exception as e:
	print ("day not formed"+ str(e))	

try:
	d7=Day.objects.create(day="Sunday").save()
except Exception as e:
	print ("day not formed"+ str(e))	


"""
BusTiming TestCase

"""
try:
	b1=BusTiming.objects.create(bus_route="PBWT-BHM-ADMN" , from_time = "06:34:57" , bus_no = "B4" , Starting_point = Place.objects.all()[0], ending_point=Place.objects.all()[0] ,  availability = "Monday" , working_day=True).save()
except Exception as e:
	print ("BusTiming not formed"+ str(e))

try:
	b2=BusTiming.objects.create(bus_route="PBWT-AG-ADMN" , from_time = "06:34:57" , bus_no = "B6" , Starting_point = Place.objects.all()[2], ending_point=Place.objects.all()[0] ,  availability = "Sunday" , working_day=False).save()
except Exception as e:
	print ("BusTiming not formed"+ str(e))

try:
	b3=BusTiming.objects.create(bus_route="JG-BHM-ADMN" , from_time = "06:34:57" , bus_no = "B8" , Starting_point = Place.objects.all()[4], ending_point=Place.objects.all()[0] ,  availability = "Wednesday" , working_day=True).save()
except Exception as e:
	print ("BusTiming not formed"+ str(e))



"""
TheftReport TestCase

"""
try:
	t1=TheftReport.objects.create(vehicle_pass_no="1234" , reporter=User.objects.all()[0] , theft_time=datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S'), theft_place="core1" , remarks="none" ,status="found" ).save()
except Exception as e:
	print ("theft not reported"+ str(e))

try:
	t2=TheftReport.objects.create(vehicle_pass_no="5352" , reporter=User.objects.all()[2] , theft_time=datetime.strptime('2015-07-05 06:36:57','%Y-%m-%d %H:%M:%S'), theft_place="core2" , remarks="none" ,status="found" ).save()
except Exception as e:
	print ("theft not reported"+ str(e))

try:
	t3=TheftReport.objects.create(vehicle_pass_no="4242" , reporter=User.objects.all()[3] , theft_time=datetime.strptime('2015-07-05 06:37:57','%Y-%m-%d %H:%M:%S'), theft_place="Admin" , remarks="none" ,status="not found" ).save()
except Exception as e:
	print ("theft not reported"+ str(e))

try:
	t4=TheftReport.objects.create(vehicle_pass_no="4235" , reporter=User.objects.all()[0] , theft_time=datetime.strptime('2015-07-05 06:38:57','%Y-%m-%d %H:%M:%S'), theft_place="hostel" , remarks="none" ,status="not found" ).save()
except Exception as e:
	print ("theft not reported"+ str(e))



