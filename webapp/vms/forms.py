from vms import models
from django.contrib.auth.models import User
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget, DateWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import TabHolder, Tab, Div, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, InlineCheckboxes
from crispy_forms.bootstrap import Accordion, AccordionGroup

class SuspiciousVehicleForm(forms.ModelForm):
    """
    User form for Reporting Suspicious Vehicle
    """

    class Meta:
        model = models.SuspiciousVehicle
        exclude = ('reporter',)
        widgets = {
            'remarks': forms.Textarea(attrs={'rows':6}),
            
        }
        labels = {
            'vehicle_image': _('Vehicle Photo'),
            'vehicle_number': _('Registration Number'),
            'vehicle_type': _('Vehicle Type'),
            'vehicle_model': _('Vehicle Model'),
        }


    def __init__(self, *args, **kwargs):
        super(SuspiciousVehicleForm, self).__init__(*args, **kwargs)
        for index, field in enumerate(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'tabindex': index+1,
            })

class PersonPassForm(forms.ModelForm):
    """
    Admin form for Blocking Passes
    """

    class Meta:
        model = models.PersonPass
        exclude = ('is_blocked',)
        widgets = {
            'expiry_date': DateWidget(usel10n = True, bootstrap_version=3,),
            'issue_date': DateWidget(usel10n = True, bootstrap_version=3,),
          
        }
        labels = {
            'user_photo': _('Your photo'),
            'old_card_reference': _('Old Card Number'),
            'age': _('Age'),
            'pass_number': _('Pass Number'),
            'name': _('Name'),
            'identified_by': _('Office'),
            'work_area': _('Work Area'),
            'working_time': _('Working Time'),
            'nature_of_work': _('Job'),
        }

 
    def __init__(self, *args, **kwargs):
        super(PersonPassForm, self).__init__(*args, **kwargs)
        for index, field in enumerate(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'tabindex': index+1,
            })
        

class TheftForm(forms.ModelForm):
    """
    User form for reporting theft
    """

    class Meta:
        model = models.TheftReport
        exclude = ('reporter', 'status')
        widgets = {
            'theft_time': DateTimeWidget(usel10n = True, bootstrap_version=3),
            'remarks': forms.Textarea(attrs={'rows':6}),
        }

    def __init__(self, *args, **kwargs):
        super(TheftForm, self).__init__(*args, **kwargs)
        for index, field in enumerate(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'tabindex': index+1,
            })

class StudentVehicleForm(forms.ModelForm):
    """
    Student form for registering vehicle
    """

    class Meta:
        model = models.StudentVehicle
        exclude = ('registered_with_security_section',)
        dateOptions = {
            'startView': 4,
        }
        widgets = {
            'date_of_birth': DateWidget(usel10n = True, bootstrap_version=3,
                                        options = dateOptions),
            'insurance_valid_upto': DateWidget(usel10n = True, bootstrap_version=3,
                                               options = dateOptions),
            'driving_license_issue_date': DateWidget(usel10n = True,
                                                    bootstrap_version=3,
                                                    options = dateOptions),
            'driving_license_expiry_date': DateWidget(usel10n = True,
                                                      bootstrap_version=3,
                                                      options = dateOptions),
            'remarks': forms.Textarea(attrs={'rows':6}),
            'address_of_communication': forms.Textarea(attrs={'rows':4}),
            'permanent_address': forms.Textarea(attrs={'rows':4}),
            'declaration': forms.Textarea(attrs={'rows':6,
                                                 'readonly':True,
                                                 'style':'resize:none;',}),
        }
        labels = {
            'user_photo': _('Your photo'),
            'address_of_communication': _('Address'),
            'address_of_communication_district': _('District'),
            'address_of_communication_state': _('State'),
            'address_of_communication_pincode': _('Pincode'),
            'permanent_address': _('Address'),
            'permanent_address_district': _('District'),
            'permanent_address_state': _('State'),
            'permanent_address_pincode': _('Pincode'),
            'parents_contact_no': _('Contact number'),
            'parents_emailid': _('Email ID'),
            'vehicle_registration_number': _('Registration Number'),
            'driving_license_number': _('License number'),
            'driving_license_issue_date': _('Issue date'),
            'driving_license_expiry_date': _('Expiry Date'),
            'driving_license': _('Scanned copy'),
        }

    def __init__(self, *args, **kwargs):
        super(StudentVehicleForm, self).__init__(*args, **kwargs)
        for index, field in enumerate(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'tabindex': index+1,
            })
        for field in self.fields.values():
            field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_student_vehicle_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2 col-md-offset-1'
        self.helper.field_class = 'col-md-4'
        self.helper.form_method = 'post'
        self.helper.form_action = '/vms/users/submit-vehicle-registration/'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Personal Details',
                    'name', 
                    'roll_number',
                    'department',
                    'programme',
                    'date_of_birth',
                    'hostel_name',
                    'room_number',
                    'mobile_number',
                    'user_photo',
                    'identity_card',
                ),
                Tab('Contact',

                    Accordion(
                        AccordionGroup('Address of communication',
                            'address_of_communication',
                            'address_of_communication_district',
                            'address_of_communication_state',
                            'address_of_communication_pincode',
                        ),
                        AccordionGroup('Permanent Address',
                            'permanent_address',
                            'permanent_address_district',
                            'permanent_address_state',
                            'permanent_address_pincode',
                        ),
                        AccordionGroup('Parent/Guardian Details',
                            'parents_contact_no',
                            'parents_emailid',
                        ),
                    ),
                ),
                Tab('Vehicle Details',
                    'vehicle_registration_number',
                    'registered_with_security_section',
                    'color',
                    'make_and_model',
                    'chassis_number',
                    'engine_number',
                    'registered_in_the_name_of',
                    'relation_with_owner',
                    'vehicle_insurance_no',
                    'insurance_valid_upto',
                    'vehicle_registration_card',
                    'vehicle_insurance',
                    'vehicle_photo',
                ),
                Tab('Driving License',
                    'driving_license_number',
                    'driving_license_issue_date',
                    'driving_license_expiry_date',
                    'driving_license',
                    'declaration'
                )
            ),
            ButtonHolder(
                Submit('submit', 'Submit',
                       css_class='btn-primary col-md-offset-5 form-submit')
            )
        )