from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .forms import TheftForm, StudentVehicleForm, PersonPassForm, BusTimingForm, EmployeeVehicleForm
from .models import TheftReport, StudentVehicle, EmployeeVehicle, BusTiming, Guard, Place, ParkingSlot, PersonPass, OnDutyGuard, Gate, StudentCycle
from datetime import datetime
from django.forms.models import model_to_dict
from itertools import chain
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

@login_required(login_url="/vms/")
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

@login_required(login_url="/vms/")
def add_guards(request):
    return HttpResponse("CSV Upload to be included")

@login_required(login_url="/vms/")
def update_bus_details(request):    
    if request.method == "POST":
        form = BusTimingForm(data=request.POST)
        if form.is_valid():
            form.save()
            form2 = BusTimingForm()
            return render(request, 'admin/bustiming.html', {
                'message': "Bus Timings updated successfully",                
                'form': form2,
                })
        else:
            form2 = BusTimingForm()
            return render(request, 'admin/bustiming.html', {
                'message': "Sorry, your given timings could not be updated",
                'form': form2,
                })
    else:
        form = BusTimingForm()
        places = Place.objects.all()
        return render(request, 'admin/bustiming.html', {
            'form': form,
            'places': places,
            })

@login_required(login_url="/vms/")
def upload_log(request):
    pass


def issue_pass(request):
    if request.method == "POST":
        form = PersonPassForm(request.POST,request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.is_blocked = False
            task.save()
            form2 = PersonPassForm()
            messages.success(request, "Pass creation completed successfully")
            return render(request, 'admin/issue_pass.html', {
                'form': form2,
                })
        else:
            messages.warning(request, "Unable to generate pass successfully")
            return render(request, 'admin/issue_pass.html',{
            'form':form,
            })

    else:
        form=PersonPassForm()
        return render(request, 'admin/issue_pass.html',{
            'form':form,
            })


@login_required(login_url="/vms/")
def parking_slot_update(request):
    if request.method == "POST":
        parkings=ParkingSlot.objects.all()
        parking=parkings.get(parking_area_name=request.POST['parking_area_name'])
        if request.POST['total_slots'] < request.POST['available_slots'] or int(request.POST['total_slots']) <= 0 or int(request.POST['available_slots']) <=0 :
            return render(request, 'admin/parking_slot_update.html',{
                'parkings':parkings,
                'parking1':parkings[0],
                'message':"Enter valid slot details for "+str(request.POST['parking_area_name'])
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

@login_required(login_url="/vms/")
def guards_on_duty(request):
    guards = Guard.objects.all()
    places = Place.objects.all()
    gates = Gate.objects.all()
    if request.method == "POST":
        try:
            user=User.objects.get(username=request.POST['guard_name'])
            guard=Guard.objects.get(guard_user=user)
            temp=Place.objects.filter(place_name=request.POST['place'])
            ondutyguard=OnDutyGuard.objects.filter(guard=guard)
            is_gate=False
            if len(temp) == 0:
                temp = Gate.objects.filter(gate_name=request.POST['place'])
                place=temp[0]
                is_gate=True
            else:
                place=temp[0]
                
            if len(ondutyguard) == 0 and is_gate:
                OnDutyGuard.objects.create(guard=guard, place=place.gate_name, is_gate=is_gate)
            elif len(ondutyguard) == 0 and not is_gate:
                OnDutyGuard.objects.create(guard=guard, place=place.place_name, is_gate=is_gate)
            else:
                update=OnDutyGuard.objects.get(guard=guard)
                if is_gate:
                    update.place=place.gate_name
                else:
                    update.place=place.place_name
                update.is_gate=is_gate
                update.save()
                messages.success(request, "Guard has been alloted the duty.")
            return render(request, 'admin/onduty_guards.html',{
                'guards':guards,
                'places':places,
                'gates':gates,
                })   
        except:
            messages.error(request, "Username not found")

    return render(request, 'admin/onduty_guards.html', {
        'guards': guards,
        'places':places,
        'gates':gates,
        })


@login_required(login_url="/vms/")
def security(request):
    guards=Guard.objects.all()
    return render(request, 'admin/security.html',{
        'guards':guards,
        'user':request.user,
        })

@login_required(login_url="/vms/")
def registered_vehicles(request):
    """
    DUMMY: Function to display all the registered vehicles to the admin
    """
    return render(request, 'admin/registered.html', {
        'username': request.user.username,
        'is_admin': True,
        })

@login_required(login_url="/vms/")
def process_empl_vehicle_registration(request, empl_vehicle_id):
    obj = EmployeeVehicle.objects.get(id=empl_vehicle_id)    
    reg_form = EmployeeVehicleForm(data=model_to_dict(obj))
    reg_form.driving_license = obj.driving_license
    #print str(reg_form.driving_license) + "\n-------------------\n\n\n\n"    
    #print str(reg_form) + "\n\n\n\n\n\n\n"
    return render(request, 'admin/process.html', {
        'readonly': True,
        'form': reg_form,
        'type': 'stud' if obj.user.user.is_student else 'empl',
        'reg_id': empl_vehicle_id,
        })

@login_required(login_url="/vms/")
def process_stud_vehicle_registration(request, student_vehicle_id):
    obj = StudentVehicle.objects.get(id=student_vehicle_id)
    reg_form = StudentVehicleForm(data=model_to_dict(obj))
    reg_form.driving_license = obj.driving_license
    #print str(reg_form.driving_license) + "\n-------------------\n\n\n\n"    
    #print str(reg_form) + "\n\n\n\n\n\n\n"
    return render(request, 'admin/process.html', {
        'readonly': True,
        'form': reg_form,
        'type': 'stud' if obj.user.user.is_student else 'empl',
        'reg_id': student_vehicle_id,
        })

@csrf_exempt
@login_required(login_url="/vms/")
def approve_reg(request, vehicle_id):
    if "stud" in request.path:
        obj = StudentVehicle.objects.get(id=vehicle_id)        
    else:
        obj = EmployeeVehicle.objects.get(id=vehicle_id)
    obj.registered_with_security_section = True
    obj.vehicle_pass_no = str(vehicle_id)
    obj.issue_date = datetime.now()
    d = datetime.now()    
    d = d.replace(year=d.year+1)    
    obj.expiry_date = d
    obj.save()
    return render(request, 'admin/old_registered.html', {
        'message': "Vehicle successfully approved. Pass generation and assignment completed successfully.",
        })

@csrf_exempt
@login_required(login_url="/vms/")
def deny_reg(request, vehicle_id):
    if "stud" in request.path:
        obj = StudentVehicle.objects.get(id=vehicle_id)        
    else:
        obj = EmployeeVehicle.objects.get(id=vehicle_id)
    obj.registered_with_security_section = False
    obj.vehicle_pass_no = str(vehicle_id)
    obj.issue_date = datetime.now()
    d = datetime.now()    
    d = d.replace(year=d.year-1)    
    obj.expiry_date = d
    obj.save()
    return render(request, 'admin/old_registered.html', {
        'message': "Vehicle application successfully denied.",
        })

@login_required(login_url="/vms/")
def registered_vehicles(request):
    """
    Function to display all the registered vehicles to the admin
    """
    stud_regs = StudentVehicle.objects.filter(registered_with_security_section=None)
    empl_regs = EmployeeVehicle.objects.filter(registered_with_security_section=None) 
    return render(request, 'admin/registered.html', {
        'username': request.user.username,
        'num_stud_regs': len(stud_regs),
        'num_empl_regs': len(empl_regs),
        'stud_regs': stud_regs,
        'empl_regs': empl_regs,        
        })

@login_required(login_url="/vms/")
def old_registered_vehicles(request):
    stud_reg_veh = StudentVehicle.objects.filter(registered_with_security_section=True)
    empl_reg_veh = EmployeeVehicle.objects.filter(registered_with_security_section=True)
    stud_cycles = StudentCycle.objects.all()
    return render(request, 'admin/old_registered.html', {
        'username': request.user.username,
        'stud_reg_veh': stud_reg_veh,
        'empl_reg_veh': empl_reg_veh,
        'stud_cycles':stud_cycles,
        })

def csventer(request):
    form=DocumentForm()
    return render_to_response('list.html',{'type':'type','form':form},context_instance=RequestContext(request))
def uploadcsv(request):
    return render_to_response('admin/csv.html',
                 {'type':"type" },context_instance=RequestContext(request))

def viewcsv(request):
    # Handle file upload
    if request.method == 'POST':
        f=request.FILES['docfile']
        #form = DocumentForm(request.POST, request.FILES)
        # handle_uploaded_file(request.FILES['file'])
        #jainam=f.read()
        if f.name.split('.')[-1]!="csv":
            return HttpResponse("File not in proper format") 
        with open('/git/vehicle-webapp/webapp/vms', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    #checkcsv('/home/fireman/Django-1.6/mysite/article/jai.csv')
        
    import csv
    
    #csvfile(jai)
    jai=open('/git/vehicle-webapp/webapp/vms','r')
    data=[j for j in csv.reader(jai)]
    jai.close()
    #dataReader=csv.reader(open('/home/fireman/Django-1.6/mysite/article/jai.csv'),delimiter=',',quotechar='"')
    for row in data:
        if row[0]=="" or row[1]=="":
            return HttpResponse("wrong Format")
    for row in data:
        test=Guard()
        #return HttpResponse("dataReasd") 
        #return HttpResponse(row[0])
        
        test.guard_user=row[0]
        test.guard_phone_number=row[1]
        
        test.save()
    return HttpResponseRedirect("../security/viewlog")
    #return HttpResponse("dataReader")  
    
    return render_to_response('enter_log.html', {'form': 'form'})    

