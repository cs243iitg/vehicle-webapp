from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .forms import TheftForm, StudentVehicleForm
from .models import TheftReport, StudentVehicle, BusTiming, Guard, Place, ParkingSlot
from datetime import datetime

#------------------------------------------------------------
#       User Authentication
#------------------------------------------------------------


@login_required(login_url="/vms/")
def cancel_theft_report(request, theft_report_id):
    """
    Cancels theft report with specified id
    """
    theft_report = TheftReport.objects.get(id=theft_report_id)
    if request.user == theft_report.reporter:
        theft_report.delete()
    return HttpResponseRedirect("/users/user_theft_reports")

#------------------------------------------------------------
#       Student Vehicle Registration
#------------------------------------------------------------

@login_required(login_url="/vms/")
def cancel_student_vehicle_registration(request, student_vehicle_id):
    """
    Cancels student's vehicle registration of specified id
    """
    student_vehicle = StudentVehicle.objects.get(id=student_vehicle_id)
    if request.user == student_vehicle.registered_in_the_name_of:
        student_vehicle.delete()
    return HttpResponseRedirect("/vms/users/your-vehicle-registrations")

def block_passes(request):
    pass

def add_guards(request):
    return HttpResponse("CSV Upload to be included")

def update_bus_details(request):
    pass

def upload_log(request):
    pass

def parking_slot_update(request):
    if request.method == "POST":

    parkings=ParkingSlot.objects.all()
    return render(request, 'admin/parking_slot_update.html',{
        'parkings':parkings,
        'parking1':parkings[0],
        })

def guards_on_duty(request):
    pass

def security(request):
    guards=Guard.objects.all()
    return render(request, 'admin/security.html',{
        'guards':guards,
        'user':request.user,
        })

def registered_vehicles(request):
    """
    DUMMY: Function to display all the registered vehicles to the admin
    """
    return render(request, 'admin/registered.html', {
        'username': request.user.username,
        'is_admin': True,
        })

