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
from .forms import TheftForm, StudentVehicleForm, EmployeeVehicleForm, StudentCycleForm
from .models import TheftReport, StudentVehicle, BusTiming, StudentCycle
from datetime import datetime
from django.db import IntegrityError

@login_required(login_url="/vms/")
def register_cycle(request):
    if request.method == "POST":
        form = StudentCycleForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            num = len(StudentCycle.objects.all())
            hostel = str(request.POST['hostel'])
            task.cycle_pass_no = str(hostel[0:3]+"-"+request.POST['room_number'])
            try:
                task.save()
                messages.success(request,"Cycle is registered successfully")
            except IntegrityError as e:
                messages.error(request, "You can register only one cycle in your name")
            
            return render(request, 'users/register_cycle.html',{
                'user':request.user,
                'form':form,
                })
    else:
        form = StudentCycleForm()
        return render(request, 'users/register_cycle.html',{
            'user':request.user,
            'form':form,
            })


@login_required(login_url="/vms/")
def register_vehicle(request):
    """
    Displays form for registering vehicle -- NOTE: This form is common to users and admin
    """
    if request.method == 'POST':
        if request.user.user.is_student:
            form = StudentVehicleForm(request.POST, request.FILES)
        else:
            form = EmployeeVehicleForm(request.POST, request.FILES)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.date_of_application = datetime.now().date()
            task.vehicle_pass_no = "Not generated"
            task.registered_with_security_section = None
            task.save()
            # print "trying to save the original form instance \n\n\n"
            # form.save_m2m()
            messages.success(request,
                'Your vehicle registration is sent to security for ' + 
                'processing. You will be contacted through your webmail.')
            if request.user.user.is_student:
                return HttpResponseRedirect("/vms/users/your-vehicle-registrations")
            else:
                return HttpResponseRedirect("/vms/admin/registered-vehicles")
        # else:
        #     return HttpResponse("form is invalid")
    elif request.user.user.is_student == True:
        form = StudentVehicleForm()
    else:
        form = EmployeeVehicleForm()
        
    return render(request, "users/register.html", {
        'form':form,        
    })

@login_required(login_url="/vms/")
def vehicle_registrations(request):
    """
    Displays vehicle registrations of a user
    """
    if request.user.user.is_student:
        print("here")
        registrations = StudentVehicle.objects.filter(user=request.user)
    else:
        registrations = EmployeeVehicle.objects.filter(user=request.user)
    print(len(registrations))
    #print(registrations.registered_with_security_section)
    return render_to_response("users/vehicle_registrations.html", {
        "registrations": registrations,        
    }, context_instance=RequestContext(request))


def user_theft_reports(request):
    reports = TheftReport.objects.filter(reporter=request.user)
    return render(request, "vms/theft_reports.html", {
        'reports': reports,
        # 'initSearch': reports[0].id if len(reports) > 0 else ""
        'initSearch':str(request.user.first_name),
    })

def cancel_theft_report(request):
	pass

def cancel_vehicle_registration(request):
	pass