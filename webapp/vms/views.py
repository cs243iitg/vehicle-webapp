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
from .forms import TheftForm, StudentVehicleForm, SuspiciousVehicleForm
from .models import TheftReport, StudentVehicle, BusTiming, EmployeeVehicle, SuspiciousVehicle, Guard
from datetime import datetime
import requests, threading


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

    return render(request, 'vms/dashboard.html',{
        'username': request.user.first_name,
        'is_user': True,
        'user': request.user,
        'buses': buses[0:3],        
    })

@login_required(login_url="/vms/")
def busdetails(request):
    return render(request, 'vms/busdetails.html')


#Ayush Mananiya
#----------thread function for sending sms---------------------------------------------
def send_sms(message, numbers):
    proxy = "http://sumeet.ranka:weh,hftg@202.141.80.24:3128"             #change the username and password
    status1=''
    for i in numbers:
        response = requests.get("https://site2sms.p.mashape.com/index.php?msg="+message+"&phone="+str(i)+"&pwd=CS243iitg&uid=8011035945",headers={"X-Mashape-Key": "CW4gX5MRw2mshX6uxzLHMxEVoB0Op1v4cMrjsnZoeRXbk3LD46", "Accept": "application/json"},proxies={"http":proxy,"https":proxy,"ftp":proxy},)
        try:
            status1 = status1 + str(response.json())
        except ValueError:
            continue
    f= open('/2.txt', 'a')
    f.write(status1+'message is sent')
    f.close()
#-------------------------end-----------------------------------------------------  

@login_required(login_url="/vms/")
def theft_report_form(request):
    """
    Displays theft report form for user -- NOTE: This form is common to admin and user
    """
    if request.method == 'POST':
        form = TheftForm(request.POST)
        if form.is_valid():
            task = form.save(commit = False)
            task.reporter = request.user
            if request.user.user.is_student:
                vehicles=StudentVehicle.objects.filter(user=request.user)
                try:
                    vehicle = StudentVehicle.objects.get(vehicle_pass_no=task.vehicle_pass_no)
                except:
                    vehicle = None
            else:
                vehicles=EmployeeVehicle.objects.filter(user=request.user)
                try:
                    vehicle = EmployeeVehicle.objects.get(vehicle_pass_no=task.vehicle_pass_no)
                except:
                    vehicle = None
            
            if vehicle != None and vehicle in vehicles:
                if request.user.user.is_student:
                    task.stud_vehicle=vehicle
                else:
                    task.emp_vehicle=vehicle

                #ayush Mananiya
    #my funct started--------------------------------------------------------------------------
                numbers = list(Guard.objects.values_list('guard_phone_number', flat=True)) #retrieves the phone numbers of all the guards
                message =  vehicle.make_and_model +' '+ task.vehicle_pass_no + ' is stolen from ' + task.theft_place +' at '+ str(task.theft_time.strftime('%d-%b-%Y %H:%M'))   #extract the form fields and generate message text
                sms_thread = threading.Thread(target=send_sms, args=(message, numbers)) #threading
                sms_thread.start()
    #ended here--------------------------------------------------------------------------------------------------------------------------
                task.save()
                messages.success(request, 'Your theft report is submitted.')
                return render(request, "vms/theft.html",{
                    'message':"Theft Report successfully submitted.",
                    'user':request.user,
                    'form':form,
                    }) 
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
    return render(request, "vms/theft_reports.html", {
        'reports': reports,
        'is_student':request.user.user.is_student,
    })

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
    Function to report suspicious vehicles
    """
    if request.method == 'POST':
        form = SuspiciousVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit = False)
            task.reporter=request.user
            task.save()
            return render(request, 'vms/suspicious.html',{
                'user':request.user,
                'form':form,
                'message':"Vehicle has been reported. Thanks for the caution."
                })

    else:
        form=SuspiciousVehicleForm()
    return render(request, 'vms/suspicious.html', {
        'user': request.user,
        'form':form,
        })

def suspicious_vehicles(request):
    """
    Function to allow users to view all suspicious reported activity
    """
    str1=""
    if request.POST:
        SuspiciousVehicle.objects.get(id=request.POST['Delete']).delete()
        vehicles = SuspiciousVehicle.objects.all()
        messages.success(request,"Report for suspicious activity is deleted")
        return render(request, 'vms/suspicious_vehicles.html',{
            'user':request.user,
            'vehicles':vehicles,
            })
        
    else:
        vehicles = SuspiciousVehicle.objects.all()
        return render(request, 'vms/suspicious_vehicles.html', {
            'user': request.user,
            'vehicles':vehicles,
            })

def delete_suspicious_vehicles(request, suspicious_vehicle_id):
    SuspiciousVehicle.objects.get(id=suspicious_vehicle_id).delete()
    pass


