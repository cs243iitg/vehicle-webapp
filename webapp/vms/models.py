from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
from django.utils.translation import ugettext_lazy as _
import os


# Create your models here.

class IITGUser(models.Model):
    user=models.OneToOneField(User)
    is_student = models.BooleanField(_('Is student'), default=False,
        help_text=_('Designates whether the user is a student or a professor.'))
    is_security = models.BooleanField(_('Is security personnal'), default=False,
        help_text=_('Designates whether this user is security personnal or not.'))

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
    hostel_name = models.CharField(max_length=32)
    room_number = models.CharField(max_length=5)
    mobile_number = models.IntegerField()
    user_photo = models.ImageField()
    identity_card = models.FileField(upload_to='identity_card')
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
    vehicle_registration_number = models.CharField(max_length=100)
    color = models.CharField(max_length=32)
    make_and_model = models.CharField(max_length=100)
    chassis_number = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100)
    registered_in_the_name_of = models.CharField(max_length=100)
    relation_with_owner = models.CharField(max_length=32)
    vehicle_insurance_no = models.CharField(max_length=100)
    insurance_valid_upto = models.DateField()
    vehicle_registration_card = models.FileField(
        upload_to='vehicle_registration_card')
    vehicle_insurance = models.FileField(upload_to='vehicle_insurance')
    vehicle_photo = models.ImageField()
    """
    Driving License
    """
    driving_license_number = models.CharField(max_length=15)
    driving_license_issue_date = models.DateField()
    driving_license_expiry_date = models.DateField()
    driving_license = models.FileField(upload_to='driving_license')
    declaration = models.TextField(blank=True, null=True,
        default="By submitting this form, I hereby declare that " +
                "I will be obliged to the following terms and conditions:\n\n" +
                "1) I will abide by the rules of Traffic,\n" +
                "2) I will not cause inconvenience to other road users.")
    
    date_of_application = models.DateTimeField(blank=True, null=True)
    registered_with_security_section = models.BooleanField()
    vehicle_pass_no = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name

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
    identity_card = models.FileField(upload_to='identity_card')
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
    vehicle_insurance_no = models.CharField(max_length=100)
    insurance_valid_upto = models.DateField()
    vehicle_registration_card = models.FileField(
        upload_to='vehicle_registration_card')
    vehicle_insurance = models.FileField(upload_to='vehicle_insurance')
    vehicle_photo = models.ImageField()
    """
    Driving License
    """
    driving_license_number = models.CharField(max_length=15)
    driving_license_issue_date = models.DateField()
    driving_license_expiry_date = models.DateField()
    driving_license = models.FileField(upload_to='driving_license')
    declaration = models.TextField(blank=True, null=True,
        default="By submitting this form, I hereby declare that " +
                "I will be obliged to the following terms and conditions:\n\n" +
                "1) I will abide by the rules of Traffic,\n" +
                "2) I will not cause inconvenience to other road users.")
    
    date_of_application = models.DateTimeField(blank=True, null=True)
    registered_with_security_section = models.BooleanField()
    vehicle_pass_no = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name

class Guard(models.Model):
    """
    Details of all security guards
    """
    guard_name = models.CharField(max_length=255)
    guard_phone_number=models.IntegerField()

    def __str__(self):
        return self.guard_name

class Gate(models.Model):
    """
    Entry/Exit gates for vehicles
    """
    gate_name = models.CharField(max_length=50)
    security_on_duty = models.ForeignKey(Guard, blank=True, null=True)

    def __str__(self):
        return self.gate_name


class ParkingSlot(models.Model):
    """
    Details of parking slot along with number of vehicles
    """
    parking_area_name = models.CharField(max_length = 100)
    security_on_duty = models.ForeignKey(Guard, blank=True, null=True)
    total_slots = models.IntegerField(default=0, blank=True, null=True)
    available_slots = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.parking_slot_name

class VehiclePass(models.Model):

    pass_number=models.CharField(max_length=10)
    vehicle_no=models.CharField(max_length=20)
    issue_date=models.DateField()
    expiry_date=models.DateField()
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
    def __str__(self):
        return self.pass_numer

class PersonPass(models.Model):
    old_card_reference=models.CharField(max_length=10)
    pass_number=models.CharField(max_length=10) 
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
    def __str__(self): 
        return self.pass_number

class SuspiciousVehicle(models.Model):
    """
    Details of suspicious vehicle
    """
    reporter=models.ForeignKey(User)
    vehicle_number = models.CharField(max_length=20)
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
    vehicle_image = models.ImageField(blank=True, null=True)
    remarks = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.vehicle_number


class ResidentLog(models.Model):
    """
    Log for residents of the campus
    """
    registration_number = models.CharField(max_length=50)
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
    gate = models.ForeignKey(Gate, null=True)
    is_entering = models.BooleanField('Is the vehicle entering?')

    def __str__(self):
        return self.registration_number


class VisitorLog(models.Model):
    """
    Log of visitors for additional details
    """
    vehicle_number = models.CharField(max_length=20)
    in_gate = models.ForeignKey(Gate, related_name='in_gate_log', null=True)
    out_gate = models.ForeignKey(Gate, related_name='out_gate_log', null=True)
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
    registration_number = models.CharField(max_length=50)
    reporter = models.ForeignKey(User, blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, null=True,
                                    choices=[
                                        ('bicycle', 'bicycle'),
                                        ('bike', 'bike'),
                                        ('car', 'car'),
                                        ('truck', 'truck'),
                                        ('courier', 'courier'),
                                        ('auto', 'auto'),
                                        ('other', 'other'),
                                    ])
    vehicle_model = models.CharField(max_length=100, null=True)
    theft_time = models.DateTimeField(blank=True, null=True)
    theft_place = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=20, default="not found")


    def __str__(self):
        return self.registration_number

# class Route(models.Model):
#     place=models.ForeignKey('Place')
#     bus=models.ForeignKey('BusTiming')
#     numbering=models.PositiveSmallIntegerField()
#     class Meta:
#         ordering=('numbering',)

#     def __str__(self):
#         return str(self.place)+" "+str(self.numbering)+" "+str(self.bus)

class Place(models.Model):
    place_name=models.CharField(max_length=32)
    def __str__(self):
        return self.place_name

class Day(models.Model):
    day=models.CharField(max_length=32)
    def __str__(self):
        return self.day

class BusTiming(models.Model):

    """route contains all the passing points"""
    bus_route = models.CharField(max_length=512)
    from_time = models.TimeField()
    #to_time = models.TimeField()
    bus_no = models.CharField(max_length=10 ,blank=False)
    starting_point = models.ForeignKey('Place', related_name="starting_point")
    ending_point=models.ForeignKey('Place', related_name="ending_point")
    availability = models.ManyToManyField('Day')
    working_day=models.BooleanField()
    def __str__(self):
        return self.bus_no

