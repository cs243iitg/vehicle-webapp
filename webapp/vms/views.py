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

#------------------------------------------------------------
#       User Authentication
#------------------------------------------------------------

def login(request):
    """
    Displays login page at the start
    """
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        return render_to_response('vms/login.html', {
            'form_errors': form_errors,
        })
    else:
        return render_to_response('vms/login.html', c)


@login_required(login_url="/vms")
def logout(request):
    """
    Logs the user out, if he is logged in.
    """
    auth.logout(request)
    return HttpResponseRedirect('/vms/', {
        'form_errors': "You've succesfully logged out."
    })


def auth_view(request):
    """
    Authenticates user from the username and password from POST -- REQUIRES CHANGES DEPENDING ON MODEL
    """
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)        
        return HttpResponseRedirect('/vms/users/dashboard') #CHANGE THIS!! -- SHOULD WORK ACCORDING TO USER
    else:
        return HttpResponseRedirect('/vms/')

#------------------------------------------------------------
#       Theft Reporting for User
#------------------------------------------------------------

@login_required(login_url="/vms/")
def home(request):
    """
    Home page for user, with his previous tasks
    """
    today = str.lower(datetime.now().strftime("%A"))    
    buses = sorted(j for j in BusTiming.objects.all() if (j.from_time >= datetime.now().time() and filter(lambda x: str(x).lower() == today, j.availability.all()) ))

    return render(request, 'users/dashboard.html',{
        'username': request.user.first_name,
        'is_user': True,
        'user': request.user,
        'buses': buses[0:3],        
    })


@login_required(login_url="/vms/")
def admin_home(request):
    """
    Function to return home page of administrator
    """
    return render(request, 'admin/admin.html', {
        'username': request.user.username,
        'is_admin': True,
        })


@login_required(login_url="/vms/")
def report_theft(request):
    """
    Displays theft report form for user -- NOTE: This form is common to admin and user
    """
    if request.method == 'POST':
        form = TheftForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.reporter = request.user
            task.save()
            messages.success(request, 'Your theft report is submitted.')
            return HttpResponseRedirect("/vms/your-theft-reports")
    else:
        form = TheftForm()
    return render(request, "users/theft.html", {
        'form':form,
        'is_admin': True if request.path == "/vms/admin/theft/" else False,
        'is_user': True if request.path == "/vms/users/theft/" else False,
    })

@login_required(login_url="/vms/")
def user_theft_reports(request):
    """
    Displays to users their theft reports
    """
    reports = TheftReport.objects.filter(reporter=request.user)
    return render_to_response("users/theft_reports.html", {
        "reports": reports,
        'is_user': True,
    }, context_instance=RequestContext(request))

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
#       Theft Reports for Admin
#------------------------------------------------------------

@login_required(login_url="/vms/")
def admin_theft_reports(request):
    """
    Displays to admin all users' theft reports
    """
    reports = TheftReport.objects.all()
    return render_to_response("vms/user_theft_reports.html", {
        "reports": reports,
        'is_admin': True,
    }, context_instance=RequestContext(request))


#------------------------------------------------------------
#       Student Vehicle Registration
#------------------------------------------------------------

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
def user_vehicle_registrations(request):
    """
    Displays vehicle registrations of a user
    """
    registrations = StudentVehicle.objects.filter(
        registered_in_the_name_of=request.user)
    return render_to_response("users/vehicle_registrations.html", {
        "registrations": registrations,
        "is_user" : True,
    }, context_instance=RequestContext(request))

@login_required(login_url="/vms/")
def cancel_student_vehicle_registration(request, student_vehicle_id):
    """
    Cancels student's vehicle registration of specified id
    """
    student_vehicle = StudentVehicle.objects.get(id=student_vehicle_id)
    if request.user == student_vehicle.registered_in_the_name_of:
        student_vehicle.delete()
    return HttpResponseRedirect("/vms/users/your-vehicle-registrations")

@login_required(login_url="/vms/")
def parking_availability(request):
    """
    DUMMY: Function to serve the parking spaces that are available
    """
    return render(request, 'users/parking.html', {
        'username': request.user.username,
        'is_admin': True if request.path == "/vms/admin/register-vehicle/" else False,
        'is_user': True if request.path == "/vms/users/register-vehicle/" else False,
        })

@login_required(login_url="/vms/")
def suspicious_vehicles(request):
    """
    DUMMY: Function to report suspicious vehicles
    """
    return render(request, 'users/suspicious.html', {
        'username': request.user.username,
        'is_user': True,
        })

def admin_bustiming(request):
    """
    DUMMY: Function to allow the administrator to update the timings of busses
    """
    return render(request, 'admin/bustiming.html', {
        'username': request.user.username,
        'is_admin': True,
        })

def admin_passes(request):
    """
    DUMMY: Function to allow the administrator create/delete/update the passes issued
    """
    return render(request, 'admin/passes.html', {
        'username': request.user.username,
        'is_admin': True,
        })
def admin_logs(request):
    """
    DUMMY: Function to add logs
    """

    return render(request, 'admin/logs.html', {
        'username': request.user.username,
        'is_admin': True,
        })

def admin_suspicious_display(request):
    """
    DUMMY: Function to allow admin to view all suspicious reported activity
    """

    return render(request, 'admin/suspicious.html', {
        'username': request.user.username,
        'is_admin': True,
        })

def admin_registered_vehicles(request):
    """
    DUMMY: Function to display all the registered vehicles to the admin
    """
    return render(request, 'admin/registered.html', {
        'username': request.user.username,
        'is_admin': True,
        })
