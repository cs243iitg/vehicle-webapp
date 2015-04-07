from django.db import models
from django.contrib.auth.models import User, Group
import os


# Create your models here.
class StudentVehicle(models.Model):
    """
    Personal Details
    """
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
    registered_in_the_name_of = models.ForeignKey(User)
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

    def save(self, *args, **kwargs):
        files_uploaded = [
            "identity_card","driving_license",
            "vehicle_registration_card","vehicle_insurance"
        ]
        extensions_allowed = [".jpg",".jpeg",".png",".pdf",".gif"]
        path_identity_card = self.identity_card.path
        path_driving_license = self.driving_license.path
        path_vehicle_registration_card = self.vehicle_registration_card.path
        path_vehicle_insurance = self.vehicle_insurance.path
        if os.path.splitext(path_identity_card)[1] in extensions_allowed:
            return super(StudentVehicle,self).save(*args, **kwargs)
        if os.path.splitext(path_driving_license)[1] in extensions_allowed:
            return super(StudentVehicle,self).save(*args, **kwargs)
        if os.path.splitext(path_vehicle_registration_card)[1] \
                            in extensions_allowed:
            return super(StudentVehicle,self).save(*args, **kwargs)
        if os.path.splitext(path_vehicle_insurance)[1] in extensions_allowed:
            return super(StudentVehicle,self).save(*args, **kwargs)



class Guard(models.Model):
    """
    Details of all security guards
    """
    guard_name = models.CharField(max_length=255)

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
    parking_slot_name = models.CharField(max_length = 100)
    security_on_duty = models.ForeignKey(Guard, blank=True, null=True)
    total_slots = models.IntegerField(default=0, blank=True, null=True)
    available_slots = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.parking_slot_name


class SuspiciousVehicle(models.Model):
    """
    Details of suspicious vehicle
    """
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
    reporter_name = models.CharField(max_length=255)
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


class BusTiming(models.Model):
    route = models.CharField(max_length=255)
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return self.route
