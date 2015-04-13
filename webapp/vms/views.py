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
from .models import TheftReport, StudentVehicle, BusTiming, EmployeeVehicle
from datetime import datetime


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
def theft_report_form(request):
    """
    Displays theft report form for user -- NOTE: This form is common to admin and user
    """
    if request.method == 'POST':
        form = TheftForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.reporter = request.user
            if request.user.user.is_student:
                vehicles=StudentVehicle.objects.filter(user=request.user)
            else:
                vehicles=EmployeeVehicle.objects.filter(user=request.user)
            if task in vehicles:
                task.save()
                messages.success(request, 'Your theft report is submitted.')
                return HttpResponse("submitted")
            else:
                return HttpResponse("Not your vehicle")
    else:
        form = TheftForm()
  
    return render(request, "vms/theft.html", {
        'form':form,
        'user':request.user,
    })

@login_required(login_url="/vms/")
def vehicles_missing(request):
    """
    Displays to users their theft reports
    """
    reports = TheftReport.objects.filter(reporter=request.user)
    return render_to_response("users/theft_reports.html", {
        "reports": reports,
        'is_user': True,
    }, context_instance=RequestContext(request))

@login_required(login_url="/vms/")
def parking_slot_availability(request):
    """
    DUMMY: Function to serve the parking spaces that are available
    """
    return render(request, 'users/parking.html', {
        'username': request.user.username,
        'is_admin': True if request.path == "/vms/admin/register-vehicle/" else False,
        'is_user': True if request.path == "/vms/users/register-vehicle/" else False,
        })

@login_required(login_url="/vms/")
def suspicious_vehicle_report_form(request):
    """
    DUMMY: Function to report suspicious vehicles
    """
    return render(request, 'users/suspicious.html', {
        'username': request.user.username,
        'is_user': True,
        })

def suspicious_vehicles(request):
    """
    DUMMY: Function to allow admin to view all suspicious reported activity
    """

    return render(request, 'admin/suspicious.html', {
        'username': request.user.username,
        'is_admin': True,
        })

