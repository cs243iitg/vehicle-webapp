from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .forms import TheftForm, StudentVehicleForm
from .models import TheftReport, StudentVehicle, BusTiming
from datetime import datetime

@login_required(login_url="/vms/")
def register_vehicle(request):
    """
    Displays form for registering vehicle -- NOTE: This form is common to users and admin
    """
    if request.method == 'POST':
        form = StudentVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.date_of_application = datetime.now().date()
            task.vehicle_pass_no = "Not generated"
            task.save()
            messages.success(request,
                'Your vehicle registration is sent to security for ' + 
                'processing. You will be contacted through your webmail.')
            return HttpResponseRedirect("/vms/your-vehicle-registrations")
    else:
        form = StudentVehicleForm()
    return render(request, "users/register.html", {
        'form':form,
        'is_admin': True if request.path == "/vms/admin/register-vehicle/" else False,
        'is_user': True if request.path == "/vms/users/register-vehicle/" else False,
    })

@login_required(login_url="/vms/")
def vehicle_registrations(request):
    """
    Displays vehicle registrations of a user
    """
    registrations = StudentVehicle.objects.filter(
        registered_in_the_name_of=request.user)
    return render_to_response("users/vehicle_registrations.html", {
        "registrations": registrations,
        "is_user" : True,
    }, context_instance=RequestContext(request))

def user_theft_reports(request):
	pass

def cancel_theft_report(request):
	pass

def cancel_vehicle_registration(request):
	pass