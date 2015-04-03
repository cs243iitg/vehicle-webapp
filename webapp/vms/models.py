from django.db import models
from django.contrib.auth.models import User, Group
import os


# Create your models here.
class StudentVehicle(models.Model):
	"""
	Personal Details
	"""
	user_photo = models.ImageField()
	vehicle_photo = models.ImageField()
	name = models.CharField(max_length=255)
	roll_number = models.IntegerField()
	department = models.CharField(max_length=100)
	programme = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	hostel_name = models.CharField(max_length=32)
	room_number = models.CharField(max_length=5)
	mobile_number = models.IntegerField()
	driving_license_number = models.CharField(max_length=15)
	driving_license_issue_date = models.DateField()
	driving_license_expiry_date = models.DateField()

	"""
	Parents' Contact Details
	"""
	address_of_communication=models.TextField()
	address_of_communication_district=models.CharField(max_length=100)
	address_of_communication_state=models.CharField(max_length=100)
	address_of_communication_pincode=models.IntegerField()
	permanent_address=models.TextField()
	permanent_address_district=models.CharField(max_length=100)
	permanent_address_state=models.CharField(max_length=100)
	permanent_address_pincode=models.IntegerField()
	parents_emailid=models.EmailField(max_length=75)
	parents_contact_no=models.IntegerField()

	"""
	Vehicle Details
	"""
	vehicle_registration_number=models.CharField(max_length=100)
	registered_with_security_section=models.BooleanField()
	color=models.CharField(max_length=32)
	make_and_model=models.CharField(max_length=100)
	chassis_number=models.CharField(max_length=100)
	engine_number=models.CharField(max_length=100)
	registered_in_the_name_of=models.ForeignKey(User)
	relation_with_owner=models.CharField(max_length=32)
	vehicle_insurance_no=models.CharField(max_length=100)
	insurance_valid_upto=models.DateField()

	declaration=models.BooleanField()
	date_of_application=models.DateTimeField()

	identity_card=models.FileField(upload_to='identity_card')
	driving_license=models.FileField(upload_to='driving_license')
	vehicle_registration_card=models.FileField(upload_to='vehicle_registration_card')
	vehicle_insurance=models.FileField(upload_to='vehicle_insurance')

	vehicle_pass_no=models.CharField(max_length=32)

	def save(self, *args, **kwargs):
		files_uploaded=["identity_card","driving_license","vehicle_registration_card","vehicle_insurance"]
		extensions_allowed=[".jpg",".jpeg",".png",".pdf",".gif"]
		path_identity_card=self.identity_card.path
		path_driving_license=self.driving_license.path
		path_vehicle_registration_card=self.vehicle_registration_card.path
		path_vehicle_insurance=self.vehicle_insurance.path
		if os.path.splitext(path_identity_card)[1] in extensions_allowed:
			return super(StudentVehicle,self).save(*args, **kwargs)
		if os.path.splitext(path_driving_license)[1] in extensions_allowed:
			return super(StudentVehicle,self).save(*args, **kwargs)
		if os.path.splitext(path_vehicle_registration_card)[1] in extensions_allowed:
			return super(StudentVehicle,self).save(*args, **kwargs)
		if os.path.splitext(path_vehicle_insurance)[1] in extensions_allowed:
			return super(StudentVehicle,self).save(*args, **kwargs)





