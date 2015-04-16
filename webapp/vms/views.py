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
from .models import TheftReport, StudentVehicle, BusTiming, EmployeeVehicle, SuspiciousVehicle, Guard, ParkingSlot, StudentCycle, OnDutyGuard, PersonPass
from datetime import datetime
import requests, threading
from vms import pdf


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
# @login_required(login_url="/vms/")
# def home(request):
#     """
#     Home page for user, with his previous tasks
#     """
#     today = str.lower(datetime.now().strftime("%A"))    
#     buses = sorted(j for j in BusTiming.objects.all() if (j.from_time >= datetime.now().time() and filter(lambda x: str(x).lower() == today, j.availability.all()) ))
#     if request.user.user.is_student:
#         num_suspicious = len(SuspiciousVehicle.objects.filter(reporter=request.user))
#         x1 = [j for j in StudentVehicle.objects.all() if (j.user == request.user and j.registered_with_security_section==None)]
#         num_pending = len(x1)
#         x2 = [j.available_slots for j in ParkingSlot.objects.all()]
#         num_guards = sum(x2)
#         x3 = [j for j in TheftReport.objects.all() if j.reporter==request.user]
#         num_thefts = len(x3)

#         return render(request, 'vms/dashboard.html',{
#             'username': request.user.first_name,            
#             'user': request.user,
#             'buses': buses[0:3],  
#             'num_suspicious': num_suspicious,
#             'num_pending': num_pending,
#             'num_guards': num_guards,
#             'num_thefts': num_thefts,
#             'user_thefts': x3,
#         })
#     else:
#         num_suspicious = len(SuspiciousVehicle.objects.all())
#         num_pending = len(StudentVehicle.objects.filter(registered_with_security_section=None)) + len(EmployeeVehicle.objects.filter(registered_with_security_section=None))
#         num_approved = len(StudentVehicle.objects.filter(registered_with_security_section=True)) + len(EmployeeVehicle.objects.filter(registered_with_security_section=True))
#         num_denied = len(StudentVehicle.objects.filter(registered_with_security_section=False)) + len(EmployeeVehicle.objects.filter(registered_with_security_section=False))
#         num_guards = len(OnDutyGuard.objects.all())
#         num_thefts = len(TheftReport.objects.filter(status="Submitted"))
#         passes=PersonPass.objects.all()
#         total_blocked = len(passes.filter(is_blocked=True))
#         total_issued = len(passes.filter(is_blocked=False))
#         x = [j for j in passes if j.expiry_date < datetime.now().date()]
#         total_expired = len(x)

#         return render(request, 'vms/dashboard.html',{
#             'username': request.user.first_name,
#             'is_user': True,
#             'user': request.user,
#             'buses': buses[0:3],  
#             'num_suspicious': num_suspicious,
#             'num_pending': num_pending,
#             'num_guards': num_guards,
#             'num_thefts': num_thefts,
#             'num_approved': num_approved,
#             'num_denied': num_denied, 
#             'total_issued': total_issued,
#             'total_expired': total_expired,
#             'total_blocked': total_blocked,    
#         })



@login_required(login_url="/vms/")
def busdetails(request):
    return render(request, 'vms/busdetails.html')


#Ayush Mananiya
#----------thread function for sending sms---------------------------------------------
def send_sms(message, numbers):
    proxy = "http://sumeet.ranka:@202.141.80.24:3128"             #change the username and password
    status1=''
    for i in numbers:
        response = requests.get("https://site2sms.p.mashape.com/index.php?msg="+message+"&phone="+str(i)+"&pwd=CS243iitg&uid=8011035945",headers={"X-Mashape-Key": "CW4gX5MRw2mshX6uxzLHMxEVoB0Op1v4cMrjsnZoeRXbk3LD46", "Accept": "application/json"},proxies={"http":proxy,"https":proxy,"ftp":proxy},)
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
                cycles=StudentCycle.objects.filter(user=request.user)
                try:
                    vehicle = StudentVehicle.objects.get(vehicle_pass_no=task.vehicle_pass_no)
                    cycle=0
                except:
                    message = "Vehicle does not belong to you."
                    vehicle = None
                 
                try:    
                    vehicle = StudentCycle.objects.get(cycle_pass_no=task.vehicle_pass_no)
                    cycle=1
                except:
                    message = "Vehicle does not belong to you."
                    vehicle = None
                    return render(request, "vms/theft.html",{
                        'message':message,
                        'user':request.user,
                        'form':form,
                        }) 
            else:
                vehicles=EmployeeVehicle.objects.filter(user=request.user)
                try:
                    vehicle = EmployeeVehicle.objects.get(vehicle_pass_no=task.vehicle_pass_no)
                    cycle=0
                except:
                    vehicle = None
                    message = "Vehicle does not belong to you."
                    return render(request, "vms/theft.html",{
                        'message':message,
                        'user':request.user,
                        'form':form,
                        }) 

            
            if vehicle != None and vehicle in vehicles:
                if request.user.user.is_student:
                    task.stud_vehicle=vehicle
                else:
                    task.emp_vehicle=vehicle


                #ayush Mananiya
    #my funct started--------------------------------------------------------------------------
            if cycle == 0:
                message =  vehicle.make_and_model +' '+ task.vehicle_pass_no + ' is stolen from ' + task.theft_place +' at '+ str(task.theft_time.strftime('%d-%b-%Y %H:%M'))   #extract the form fields and generate message text
            else:
                message = vehicle.cycle_model+ ' '+vehicle.cycle_color+' '+' '+'is stolen from '+task.theft_place+' at '+ str(task.theft_time)
            numbers = list(Guard.objects.values_list('guard_phone_number', flat=True)) #retrieves the phone numbers of all the guards
            sms_thread = threading.Thread(target=send_sms, args=(message, numbers)) #threading
            sms_thread.start()
    #ended here--------------------------------------------------------------------------------------------------------------------------
            task.save()
            messages.success(request, 'Your theft report is submitted.')
            return render(request, "vms/theft.html",{
                'message':"Theft Report successfully submitted.",
                'user':request.user,
                'form':form,
                'success':True,
                'id':task.id,
                }) 
        
    else:
        form = TheftForm()
  
    return render(request, "vms/theft.html", {
        'form':form,
        'user':request.user,
    })

@login_required(login_url="/vms/")
def generate_report(request, report_id):        
    rep = TheftReport.objects.filter(id=report_id)    
    if len(rep) > 0:
        # print rep[0].theft_time
        return pdf.pdf_gen(rep[0])
        return HttpResponse("done")

@login_required(login_url="/vms/")
def vehicles_missing(request):
    """
    Displays to users their theft reports
    """
    reports = TheftReport.objects.all()
    return render(request, "vms/theft_reports.html", {
        'reports': reports,
    })

@login_required(login_url="/vms/")
def parking_slot_availability(request):
    """
    Function to serve the parking spaces that are available
    """
    return render(request, 'users/parking.html', {
        'pslots': ParkingSlot.objects.all(),
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


