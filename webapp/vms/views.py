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
from .models import TheftReport, StudentVehicle
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
    Authenticates user from the username and password from POST
    """
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/vms/home')
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
    return render_to_response('vms/home.html',{
        'username': request.user.username,
    }, context_instance=RequestContext(request))


@login_required(login_url="/vms/")
def report_theft(request):
    """
    Displays theft report form for user
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
    return render_to_response("vms/report_theft.html", {
        'form':form,
    }, context_instance=RequestContext(request))


@login_required(login_url="/vms/")
def user_theft_reports(request):
    """
    Displays to users their theft reports
    """
    reports = TheftReport.objects.filter(reporter=request.user)
    return render_to_response("vms/user_theft_reports.html", {
        "reports": reports,
    }, context_instance=RequestContext(request))

@login_required(login_url="/vms/")
def cancel_theft_report(request, theft_report_id):
    """
    Cancels theft report with specified id
    """
    theft_report = TheftReport.objects.get(id=theft_report_id)
    if request.user == theft_report.reporter:
        theft_report.delete()
    return HttpResponseRedirect("/vms/your-theft-reports")

#------------------------------------------------------------
#       Theft Reports for Admin
#------------------------------------------------------------

@login_required(login_url="/vms/")
def admin_theft_reports(request):
    """
    Displays to users their theft reports
    """
    reports = TheftReport.objects.all()
    return render_to_response("vms/user_theft_reports.html", {
        "reports": reports,
    }, context_instance=RequestContext(request))


#------------------------------------------------------------
#       Student Vehicle Registration
#------------------------------------------------------------

@login_required(login_url="/vms/")
def register_vehicle(request):
    """
    Displays form for registering vehicle
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
    return render_to_response("vms/register_student_vehicle.html", {
        'form':form,
    }, context_instance=RequestContext(request))

@login_required(login_url="/vms/")
def user_vehicle_registrations(request):
    """
    Displays vehicle registrations of a user
    """
    registrations = StudentVehicle.objects.filter(
        registered_in_the_name_of=request.user)
    return render_to_response("vms/user_vehicle_registrations.html", {
        "registrations": registrations,
    }, context_instance=RequestContext(request))

@login_required(login_url="/vms/")
def cancel_student_vehicle_registration(request, student_vehicle_id):
    """
    Cancels student's vehicle registration of specified id
    """
    student_vehicle = StudentVehicle.objects.get(id=student_vehicle_id)
    if request.user == student_vehicle.registered_in_the_name_of:
        student_vehicle.delete()
    return HttpResponseRedirect("/vms/your-vehicle-registrations")