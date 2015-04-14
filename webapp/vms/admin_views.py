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
from .forms import TheftForm, StudentVehicleForm, PersonPassForm
from .models import TheftReport, StudentVehicle, BusTiming, Guard, Place, ParkingSlot, PersonPass
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
    """
    blocks pass of the specified id
    """
    if request.method == 'POST':
        if 'block' in request.POST:
            pnum = request.POST['passnumber']
            num = PersonPass.objects.all()
            reasons = request.POST['reason']
            flag=0
            for n in num:
                if n.pass_number == pnum:
                    flag=1
            if flag == 0 or len(reasons) == 0:
                if flag == 0:
                    messages.error(request, "You have entered an invalid pass number")
                if len(reasons) == 0:
                    messages.error(request, 'Reason is required.')
            else:
                person = PersonPass.objects.get(pass_number= pnum)

                #if person is not None:
                    #if pnum == passnum.pass_number:
                    
                if person.is_blocked == False:
                    #return HttpResponse('Your have already blocked this Pass!!')
                    person.reason= reasons
                    person.is_blocked = True
                    person.save()
                   # return HttpResponse('Your have successfully blocked!!')
                    messages.success(request, 'Your have successfully blocked pass for '+ person.name)         
                else:
                    messages.error(request, 'Your have already blocked the pass for '+ person.name)  
        elif 'unblock' in request.POST:
            pnum = request.POST['passnumber']
            num = PersonPass.objects.all()
            reasons = request.POST['reason']
            flag=0
            for n in num:
                if n.pass_number == pnum:
                    flag=1
            if flag == 0 or len(reasons) == 0:
                if flag == 0:
                    messages.error(request, "You have entered an invalid pass number")
                if len(reasons) == 0:
                    messages.error(request, 'Reason is required.')
            else:
                person = PersonPass.objects.get(pass_number= pnum)
                #reasons = request.POST['reason']
                #if person is not None:
                    #if pnum == passnum.pass_number:
                    
                if person.is_blocked == True:
                    #return HttpResponse('Your have already blocked this Pass!!')
                    person.reason= reasons
                    person.is_blocked = False
                    person.save()
                   # return HttpResponse('Your have successfully blocked!!')
                    messages.success(request, 'Your have successfully unblocked the pass for '+person.name)         
                else:
                    messages.error(request, 'Your have already unblocked the Pass for '+person.name)  
                    
                #return HttpResponseRedirect("admin/block.pass.html")
        # else:    
        #     return render_to_response('admin/block.pass.html' ,{'error' : "You have entered an invalid pass number"}, context_instance=RequestContext(request))
    return render_to_response('admin/block_pass.html' , context_instance=RequestContext(request))

def add_guards(request):
    return HttpResponse("CSV Upload to be included")

def update_bus_details(request):
    pass

def upload_log(request):
    pass

def issue_pass(request):
    form=PersonPassForm()
    return render(request, 'admin/issue_pass.html',{
        'form':form,
        })

def parking_slot_update(request):
    if request.method == "POST":
        parkings=ParkingSlot.objects.all()
        parking=parkings.get(parking_area_name=request.POST['parking_area_name'])
        if request.POST['total_slots'] < request.POST['available_slots']:
            return render(request, 'admin/parking_slot_update.html',{
                'parkings':parkings,
                'parking1':parkings[0],
                'message':"Available Parking Slots cannot be more than Total number of slots for "+str(request.POST['parking_area_name'])
                })
        else:    
            parking.total_slots=request.POST['total_slots']
            parking.available_slots=request.POST['available_slots']
            parking.save()
            parkings=ParkingSlot.objects.all()
            return render(request, 'admin/parking_slot_update.html',{
                'parkings':parkings,
                'parking1':parkings[0],
                'message':"Information of the parking area is updated"
                }) 
    else:
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

