from django.test import TestCase
from vms.models import IITGUser, StudentVehicle, EmployeeVehicle , Guard, Gate, ParkingSlot, SuspiciousVehicle, ResidentLog, VisitorLog, TheftReport , VehiclePass, Place, BusTiming , PersonPass, Day
from datetime import datetime
from django.contrib.auth.models import User

<<<<<<< HEAD
"""
IITGUser TestCase

"""

=======
>>>>>>> 28d1dfd1ebcb890bf123b51c58f9ede769c39c2c
try:
	u1=IITGUser.objects.create(user=User.objects.create_user(username="sumeet",password="sumeet"),is_student=True).save()
except Exception as e:
	print ("user not formed "+ str(e))

try:
	u2=IITGUser.objects.create(user=User.objects.create_superuser(username="admin",password="admin",email="admin@admin.com")).save()
except Exception as e:
	print ("admin not formed "+ str(e))

<<<<<<< HEAD
try:
	u3=IITGUser.objects.create(user=User.objects.create_user(username="abhi",password="abhi"),is_student=True).save()
except Exception as e:
	print ("user not formed "+ str(e))

try:
	u4=IITGUser.objects.create(user=User.objects.create_user(username="eeshani",password="eeshani"),is_student=True).save()
except Exception as e:
	print ("user not formed "+ str(e))


"""
TheftReport TestCase

"""
try:
	t1=TheftReport.objects.create(registration_number="1234" , reporter=IITGUser.objects.all()[0] ,vehicle_type="bike",  vehicle_model="d-24", theft_time=datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S'), theft_place="core1" , remarks="none" ,status="found" ).save()
except Exception as e:
	print ("theft not reported"+ str(e))

try:
	t2=TheftReport.objects.create(registration_number="5352" , reporter=IITGUser.objects.all()[2] ,vehicle_type="bicycle",  vehicle_model="if-54", theft_time=datetime.strptime('2015-07-05 06:36:57','%Y-%m-%d %H:%M:%S'), theft_place="core2" , remarks="none" ,status="found" ).save()
except Exception as e:
	print ("theft not reported"+ str(e))

try:
	t3=TheftReport.objects.create(registration_number="4242" , reporter=IITGUser.objects.all()[3] ,vehicle_type="car",  vehicle_model="asd", theft_time=datetime.strptime('2015-07-05 06:37:57','%Y-%m-%d %H:%M:%S'), theft_place="Admin" , remarks="none" ,status="not found" ).save()
except Exception as e:
	print ("theft not reported"+ str(e))

try:
	t4=TheftReport.objects.create(registration_number="4235" , reporter=IITGUser.objects.all()[0] ,vehicle_type="auto",  vehicle_model="a3f", theft_time=datetime.strptime('2015-07-05 06:38:57','%Y-%m-%d %H:%M:%S'), theft_place="hostel" , remarks="none" ,status="not found" ).save()
except Exception as e:
	print ("theft not reported"+ str(e))


"""
Gate TestCase

"""
try:
	g1=Gate.objects.create(gate_name="Main gate").save()
except Exception as e:
	print ("gate not formed"+ str(e))

try:
	g2=Gate.objects.create(gate_name="K.V. gate").save()
except Exception as e:
	print ("gate not formed"+ str(e))

try:
	g3=Gate.objects.create(gate_name="ASEB gate").save()
except Exception as e:
	print ("gate not formed"+ str(e))

try:
	g4=Gate.objects.create(gate_name="Lathia Baghicha gate").save()
except Exception as e:
	print ("gate not formed"+ str(e))


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
VisitorLog TestCase

"""

try:
	v1=VisitorLog.objects.create(vehicle_number = "3456" , in_gate=Gate.objects.all()[0] , out_gate=Gate.objects.all()[0] , vehicle_type ="car" , vehicle_model= "Hyundai Verna" , driver_name="raju", license_number="24255", place_to_visit="Subansiri", purpose_of_visit="cab", in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
except Exception as e:
	print ("VisitorLog not formed "+ str(e))

try:
	v2=VisitorLog.objects.create(vehicle_number = "1256" , in_gate=Gate.objects.all()[0] , out_gate=Gate.objects.all()[1] , vehicle_type ="car" , vehicle_model= "Hyundai Verna" , driver_name="raghu", license_number="23425", place_to_visit="kameng", purpose_of_visit="cab", in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
except Exception as e:
	print ("VisitorLog not formed "+ str(e))

try:
	v3=VisitorLog.objects.create(vehicle_number = "8956" , in_gate=Gate.objects.all()[0] , out_gate=Gate.objects.all()[2] , vehicle_type ="auto" , vehicle_model= "Hyundai Verna" , driver_name="raja", license_number="34255", place_to_visit="manas", purpose_of_visit="cab", in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
except Exception as e:
	print ("VisitorLog not formed "+ str(e))

try:
	v4=VisitorLog.objects.create(vehicle_number = "3556" , in_gate=Gate.objects.all()[0] , out_gate=Gate.objects.all()[3] , vehicle_type ="bike" , vehicle_model= "Hyundai Verna" , driver_name="manoj", license_number="24345", place_to_visit="kapili", purpose_of_visit="cab", in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:00','%Y-%m-%d %H:%M:%S')).save()
except Exception as e:
	print ("VisitorLog not formed "+ str(e))


"""
ResidentLog TestCase

"""

try:
	r1=ResidentLog.objects.create(registration_number = "3456" , vehicle_type ="car" , vehicle_model= "Hyundai Verna" , gate = Gate.objects.all()[0], is_entering = True).save()
except Exception as e:
	print ("ResidentLog not formed "+ str(e))

try:
	r2=ResidentLog.objects.create(registration_number = "AS34" , vehicle_type ="bike" , vehicle_model = "Hero Honda" , gate = Gate.objects.all()[0] , is_entering = False).save()
except Exception as e:
	print ("ResidentLog not formed "+ str(e))

try:
	r3=ResidentLog.objects.create(registration_number = "CV30" , vehicle_type ="bicycle" , vehicle_model = "Ladybird" , gate = Gate.objects.all()[0] , is_entering = True).save()
except Exception as e:
	print ("ResidentLog not formed "+ str(e))

try:
	r4=ResidentLog.objects.create(registration_number = "3UI0" , vehicle_type ="other" , vehicle_model = "Tata Sumo" , gate = Gate.objects.all()[0] , is_entering = False).save()
except Exception as e:
	print ("ResidentLog not formed "+ str(e))


"""
VehiclePass TestCase

"""

try:
	vp1=VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="RJ-06 1111", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="bike").save()
except Exception as e:
	print ("VehiclePass not formed "+ str(e))

try:
	vp2=VehiclePass.objects.create(pass_number="BH-4576" , vehicle_no="AS-07 1231", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="car").save()
except Exception as e:
	print ("VehiclePass not formed "+ str(e))

try:
	vp3=VehiclePass.objects.create(pass_number="BH-4577" , vehicle_no="RJ-06 1141", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="bike").save()
except Exception as e:
	print ("VehiclePass not formed "+ str(e))

try:
	vp4=VehiclePass.objects.create(pass_number="BH-4578" , vehicle_no="AS-05 2341", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="auto").save()
except Exception as e:
	print ("VehiclePass not formed "+ str(e))


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
=======

g1=Guard.objects.create(guard_name = "ram", guard_phone_number="8011034051").save()
g2=Guard.objects.create(guard_name = "shyam", guard_phone_number="123").save()
g3=Guard.objects.create(guard_name = "Mohan", guard_phone_number="123").save()
g4=Guard.objects.create(guard_name = "sohan", guard_phone_number="123").save()

# ga1=Gate.objects.create(gate_name = "Main gate" , security_on_duty=g1).save()
# ga2=Gate.objects.create(gate_name = "K.V. gate" , security_on_duty=g2).save()
# ga3=Gate.objects.create(gate_name = "ASEB gate" , security_on_duty=g3).save()
# ga4=Gate.objects.create(gate_name = "Lathia Baghicha gate" , security_on_duty=g4).save()


# ParkingSlot.objects.create(total_slots = 30 , security_on_duty=g1 , parking_area_name = "Academic Complex" , available_slots = 12).save()
# ParkingSlot.objects.create(total_slots = 30 , security_on_duty=g2 , parking_area_name = "Admin Building" , available_slots = 6).save()
# ParkingSlot.objects.create(total_slots = 30 , security_on_duty=g3 , parking_area_name = "Core 4" , available_slots = 3).save()
# ParkingSlot.objects.create(total_slots = 30 , security_on_duty=g4 , parking_area_name = "Core 2" , available_slots = 1).save()

# ResidentLog.objects.create(registration_number = "3456" , vehicle_type ="car" , vehicle_model= "Hyundai Verna" , gate = ga1, is_entering = True).save()
# ResidentLog.objects.create(registration_number = "AS34" , vehicle_type ="bike" , vehicle_model = "Hero Honda" , gate = ga2 , is_entering = False).save()
# ResidentLog.objects.create(registration_number = "CV30" , vehicle_type ="bicycle" , vehicle_model = "Ladybird" , gate = ga3 , is_entering = True).save()
# ResidentLog.objects.create(registration_number = "3UI0" , vehicle_type ="other" , vehicle_model = "Tata Sumo" , gate = ga4 , is_entering = False).save()

# VisitorLog.objects.create(vehicle_number = "3456" , in_gate=ga1,out_gate=ga4,vehicle_type ="car" , vehicle_model= "Hyundai Verna" ,driver_name="raju",license_number="24255",place_to_visit="Subansiri",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
# VisitorLog.objects.create(vehicle_number = "1256" , in_gate=ga2,out_gate=ga1,vehicle_type ="car" , vehicle_model= "Hyundai Verna" ,driver_name="raghu",license_number="23425",place_to_visit="kameng",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
# VisitorLog.objects.create(vehicle_number = "8956" , in_gate=ga3,out_gate=ga2,vehicle_type ="auto" , vehicle_model= "Hyundai Verna" ,driver_name="raja",license_number="34255",place_to_visit="manas",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S')).save()
# VisitorLog.objects.create(vehicle_number = "3556" , in_gate=ga4,out_gate=ga3,vehicle_type ="bike" , vehicle_model= "Hyundai Verna" ,driver_name="manoj",license_number="24345",place_to_visit="kapili",purpose_of_visit="cab",in_time=datetime.strptime('2015-07-05 06:34:57','%Y-%m-%d %H:%M:%S'), out_time =datetime.strptime('2015-07-05 06:35:00','%Y-%m-%d %H:%M:%S')).save()

# Place.objects.create(place_name="PBWT-").save()
# Place.objects.create(place_name="BHM-").save()
# Place.objects.create(place_name="ADMN-").save()
# Place.objects.create(place_name="AG-").save()
# Place.objects.create(place_name="JG-").save()
# Place.objects.create(place_name="Com C-").save()

# VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="RJ-06 1111", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="bike").save()
# VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="AS-07 1231", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="car").save()
# VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="RJ-06 1141", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="bike").save()
# VehiclePass.objects.create(pass_number="BH-4575" , vehicle_no="AS-05 2341", issue_date="2015-04-09" ,  expiry_date="2015-10-09" ,vehicle_type="auto").save()

# TheftReport.objects.create(registration_number="1234" , reporter=User.objects.all()[0] ,vehicle_type="bike",  vehicle_model="d-24", theft_time=datetime.strptime('2015-07-05 06:35:57','%Y-%m-%d %H:%M:%S'), theft_place="core1" , remarks="none" ,status="found" ).save()
# TheftReport.objects.create(registration_number="5352" , reporter=User.objects.all()[0] ,vehicle_type="bicycle",  vehicle_model="if-54", theft_time=datetime.strptime('2015-07-05 06:36:57','%Y-%m-%d %H:%M:%S'), theft_place="core2" , remarks="none" ,status="found" ).save()
# TheftReport.objects.create(registration_number="4242" , reporter=User.objects.all()[0] ,vehicle_type="car",  vehicle_model="asd", theft_time=datetime.strptime('2015-07-05 06:37:57','%Y-%m-%d %H:%M:%S'), theft_place="Admin" , remarks="none" ,status="not found" ).save()
# TheftReport.objects.create(registration_number="4235" , reporter=User.objects.all()[0] ,vehicle_type="auto",  vehicle_model="a3f", theft_time=datetime.strptime('2015-07-05 06:38:57','%Y-%m-%d %H:%M:%S'), theft_place="hostel" , remarks="none" ,status="not found" ).save()
>>>>>>> 28d1dfd1ebcb890bf123b51c58f9ede769c39c2c
