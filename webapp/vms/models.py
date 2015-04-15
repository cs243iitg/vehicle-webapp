from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
from django.utils.translation import ugettext_lazy as _
import os


# Create your models here.

class IITGUser(models.Model):
    user=models.OneToOneField(User, related_name='user', default=False)
    is_student = models.BooleanField(_('Is student'), default=False,
        help_text=_('Designates whether the user is a student or a professor.'))

    def __str__(self):
        return self.user.username

class StudentCycle(models.Model):
    user=models.OneToOneField(User, related_name='cycle_user')
    cycle_model=models.CharField(max_length=32, blank=False)
    cycle_color=models.CharField(max_length=32)
    cycle_pass_no=models.CharField(max_length=10)
    hostel=models.CharField(max_length=50, blank=True, 
                                    choices=[
                                        ('Manas', 'Manas'),
                                        ('Dihing', 'Dihing'),
                                        ('Kameng', 'Kameng'),
                                        ('Umiam', 'Umiam'),
                                        ('Barak', 'Barak'),
                                        ('Brahmaputra', 'Brahmaputra'),
                                        ('Kapili', 'Kapili'),
                                        ('Siang','Siang'),
                                        ('Dibang','Dibang'),
                                        ('Lohit','Lohit'),
                                        ('Subansiri','Subansiri'),
                                        ('Dhansiri','Dhansiri'),
                                    ])
    room_number=models.CharField(max_length=5)

    def __str__(self):
        return self.cycle_pass_no

class StudentVehicle(models.Model):
    """
    Personal Details
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    roll_number = models.IntegerField()
    department = models.CharField(max_length=100)
    programme = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    hostel_name = models.CharField(max_length=32,choices=[
                                        ('Manas', 'Manas'),
                                        ('Dihing', 'Dihing'),
                                        ('Kameng', 'Kameng'),
                                        ('Umiam', 'Umiam'),
                                        ('Barak', 'Barak'),
                                        ('Brahmaputra', 'Brahmaputra'),
                                        ('Kapili', 'Kapili'),
                                        ('Siang','Siang'),
                                        ('Dibang','Dibang'),
                                        ('Siang','Siang'),
                                        ('Lohit','Lohit'),
                                        ('Subansiri','Subansiri'),
                                        ('Dhansiri','Dhansiri'),
                                    ])
    room_number = models.CharField(max_length=5)
    mobile_number = models.IntegerField()
    user_photo = models.ImageField()
    identity_card = models.FileField(upload_to='identity_card', null=True)
    """
    Parents' Contact Details
    """
    address_of_communication = models.TextField()
    address_of_communication_district = models.CharField(max_length=100)
    address_of_communication_state = models.CharField(max_length=100)
    address_of_communication_pincode = models.IntegerField()
    permanent_address = models.TextField()
    permanent_address_district = models.CharField(max_length=100)
    permanent_address_state = models.CharField(max_length=100)
    permanent_address_pincode = models.IntegerField()
    parents_contact_no = models.IntegerField()
    parents_emailid = models.EmailField(max_length=75)
    """
    Vehicle Details
    """
    vehicle_registration_number = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=32)
    make_and_model = models.CharField(max_length=100)
    chassis_number = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100)
    registered_in_the_name_of = models.CharField(max_length=100)
    relation_with_owner = models.CharField(max_length=32)
    vehicle_insurance_no = models.CharField(max_length=100, unique=True)
    insurance_valid_upto = models.DateField()
    vehicle_registration_card = models.FileField(upload_to='vehicle_registration_card', null=True)
    vehicle_insurance = models.FileField(upload_to='vehicle_insurance', null=True)
    vehicle_photo = models.ImageField()
    """
    Driving License
    """
    driving_license_number = models.CharField(max_length=15)
    driving_license_issue_date = models.DateField()
    driving_license_expiry_date = models.DateField()
    driving_license = models.FileField(upload_to='driving_license', null=True)
    declaration = models.TextField(blank=True, null=True,
        default="By submitting this form, I hereby declare that " +
                "I will be obliged to the following terms and conditions:\n\n" +
                "1) I will abide by the rules of Traffic,\n" +
                "2) I will not cause inconvenience to other road users.")
    
    date_of_application = models.DateTimeField(blank=True, null=True)
    registered_with_security_section = models.NullBooleanField(default=None)
    vehicle_pass_no = models.CharField(max_length=32, blank=True, null=True, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.vehicle_pass_no

class EmployeeVehicle(models.Model):
    """
    Personal Details
    """
    user=models.ForeignKey(User)
    name = models.CharField(max_length=255)
    employee_no=models.IntegerField()
    department = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    block_number = models.CharField(max_length=5)
    flat_number = models.CharField(max_length=5)
    mobile_number = models.IntegerField()
    user_photo = models.ImageField()
    identity_card = models.FileField(upload_to='identity_card', null=True)
    parking_slot_no =models.CharField(max_length=50)    
    """
    Vehicle Details
    """
    vehicle_registration_number = models.CharField(max_length=100)
    color = models.CharField(max_length=32)
    make_and_model = models.CharField(max_length=100)
    chassis_number = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100)
    registered_in_the_name_of = models.CharField(max_length=100)
    vehicle_insurance_no = models.CharField(max_length=100, unique=True)
    insurance_valid_upto = models.DateField()
    vehicle_registration_card = models.FileField(
        upload_to='vehicle_registration_card')
    vehicle_insurance = models.FileField(upload_to='vehicle_insurance', null=True)
    vehicle_photo = models.ImageField(null=True)
    """
    Driving License
    """
    driving_license_number = models.CharField(max_length=15)
    driving_license_issue_date = models.DateField()
    driving_license_expiry_date = models.DateField()
    driving_license = models.FileField(upload_to='driving_license', null=True)
    declaration = models.TextField(blank=True, null=True,
        default="By submitting this form, I hereby declare that " +
                "I will be obliged to the following terms and conditions:\n\n" +
                "1) I will abide by the rules of Traffic,\n" +
                "2) I will not cause inconvenience to other road users.")
    
    date_of_application = models.DateTimeField(blank=True, null=True)
    registered_with_security_section = models.NullBooleanField(default=None)
    vehicle_pass_no = models.CharField(max_length=32, blank=True, null=True, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.vehicle_pass_no

class Guard(models.Model):
    """
    Details of all security guards
    """
    guard_user = models.OneToOneField(User, related_name='guard_user')
    guard_phone_number=models.IntegerField()
    is_security=models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.guard_user.username

class OnDutyGuard(models.Model):
    guard = models.OneToOneField('Guard', related_name='guard')
    place = models.CharField(max_length=100)
    is_gate = models.BooleanField()

class Gate(models.Model):
    """
    Entry/Exit gates for vehicles
    """
    gate_name = models.CharField(max_length=50, unique=True)
    # security_on_duty = models.ForeignKey(Guard, blank=True, null=True)

    def __str__(self):
        return self.gate_name


class ParkingSlot(models.Model):
    """
    Details of parking slot along with number of vehicles
    """
    parking_area_name = models.CharField(max_length = 100, unique=True)
    # security_on_duty = models.ForeignKey(Guard, blank=True, null=True)
    total_slots = models.IntegerField(default=0, blank=True, null=True)
    available_slots = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.parking_area_name





class PersonPass(models.Model):
    old_card_reference=models.CharField(max_length=10)
    pass_number=models.CharField(max_length=10, unique=True) 
    name = models.CharField(max_length=255) 
    user_photo = models.ImageField() 
    age=models.IntegerField() 
    identified_by = models.CharField(max_length=255) 
    work_area = models.CharField(max_length=255) 
    working_time = models.CharField(max_length=255) 
    nature_of_work = models.CharField(max_length=255) 
    issue_date=models.DateField() 
    expiry_date=models.DateField() 
    is_blocked=models.BooleanField()
    reason=models.TextField(blank=True) 
    def __str__(self): 
        return self.pass_number

class SuspiciousVehicle(models.Model):
    """
    Details of suspicious vehicle
    """
    reporter=models.ForeignKey(User)
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True,
                                    choices=[
                                        ('bicycle', 'bicycle'),
                                        ('bike', 'bike'),
                                        ('car', 'car'),
                                        ('truck', 'truck'),
                                        ('courier', 'courier'),
                                        ('auto', 'auto'),
                                        ('other', 'other'),
                                    ])
    vehicle_model = models.CharField(max_length=100, blank=True, null=True)
    vehicle_image = models.ImageField(blank=True, null=True, upload_to='suspicious_image')
    remarks = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.vehicle_number


class ResidentLog(models.Model):
    """
    Log for residents of the campus
    """
    vehicle_pass_no = models.CharField(max_length=50)
    in_gate = models.ForeignKey(Gate, related_name='resident_in_gate', null=True)
    out_gate = models.ForeignKey(Gate, related_name='resident_out_gate', null=True)
    in_time = models.DateTimeField(blank=True, null=True)
    out_time = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.vehicle_pass_no

class VisitorLog(models.Model):
    """
    Log of visitors for additional details
    """
    vehicle_number = models.CharField(max_length=20)
    in_gate = models.ForeignKey(Gate, related_name='visitor_in_gate', null=True)
    out_gate = models.ForeignKey(Gate, related_name='visitor_out_gate', null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True,
                                    choices=[
                                        ('bicycle', 'bicycle'),
                                        ('bike', 'bike'),
                                        ('car', 'car'),
                                        ('truck', 'truck'),
                                        ('courier', 'courier'),
                                        ('auto', 'auto'),
                                        ('other', 'other'),
                                    ])
    vehicle_model = models.CharField(max_length=100, blank=True, null=True)
    driver_name = models.CharField(max_length=255, blank=True, null=True)
    license_number = models.CharField(max_length=20, blank=True, null=True)
    place_to_visit = models.CharField(max_length=100, blank=True, null=True)
    purpose_of_visit = models.TextField(max_length=1000, blank=True, null=True)
    in_time = models.DateTimeField(blank=True, null=True)
    out_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.vehicle_number


class TheftReport(models.Model):
    vehicle_pass_no = models.CharField(max_length=50, unique=True) #CHECK BETWEEN STUDENT AND EMPLOYEE VEHICLE
    reporter = models.ForeignKey(User, null=True) #VEHICLE SHOULD BE USERS
    stud_vehicle = models.ForeignKey('StudentVehicle', blank=True, null=True)
    emp_vehicle = models.ForeignKey('EmployeeVehicle', blank=True, null=True)
    # theft_date = models.DateField(blank=False, null=True)
    theft_time = models.DateTimeField(blank=False, null=True)
    theft_place = models.CharField(max_length=100, blank=False, null=True)
    remarks = models.TextField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=100, default="Submitted", choices=[("Submitted", "Submitted"), ("Received by Security Section", "Received by Security Section"), ("Search in Progress","Search in Progress"), ("Vehicle Found","Vehicle Found"), ("Case Closed (Vehicle Not Found)","Case Closed (Vehicle Not Found)"), ("Vehicle Returned","Vehicle Returned")])


    def __str__(self):
        return self.vehicle_pass_no

class Place(models.Model):
    place_name=models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.place_name


class Day(models.Model):
    day=models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.day

class BusTiming(models.Model):

    """route contains all the passing points"""
    bus_route = models.CharField(max_length=512)
    from_time = models.TimeField()
    #to_time = models.TimeField()
    bus_no = models.CharField(max_length=10 ,blank=False, unique=True)
    starting_point = models.ForeignKey('Place', related_name="starting_point")
    ending_point=models.ForeignKey('Place', related_name="ending_point")
    availability = models.ManyToManyField('Day')
    working_day=models.BooleanField()
    def __str__(self):
        return self.bus_no

