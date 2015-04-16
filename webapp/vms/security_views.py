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
from .models import TheftReport, StudentVehicle, BusTiming, PersonPass, VisitorLog, Gate
from datetime import datetime
from .forms import DocumentForm

@login_required(login_url='/vms/')
def log_form(request):
    gates = Gate.objects.all()
    return render_to_response('security/enter_log.html',
                 { 'gates':gates, },context_instance=RequestContext(request))

@login_required(login_url='/vms/')
def log(request):
    return render_to_response('security/viewlog.html',
                 {'logs':VisitorLog.objects.all().order_by('in_time') },context_instance=RequestContext(request))


    


@login_required(login_url='/vms/')
def passes(request):
    """
    Function to allow the administrator create/delete/update the passes issued
    """
    passes=PersonPass.objects.all()
    total_blocked = len(passes.filter(is_blocked=True))
    total_issued = len(passes.filter(is_blocked=False))
    x = [j for j in passes if j.expiry_date < datetime.now().date()]
    total_expired = len(x)
    return render(request, 'security/passes.html', {
        'username': request.user.username,
        'is_admin': True,
        'passes' :passes,
        'total_blocked': total_blocked,
        'total_expired': total_expired,
        'total_issued': total_issued,
        })


@login_required(login_url='/vms/')
def persondetails(request, pass_id):
    personpass=PersonPass.objects.get(id=pass_id)
    return render(request, 'security/person_pass.html',{
        'user':request.user,
        'passes':personpass,
        })

##Log enter view update
#def viewlog(request):
    
@login_required(login_url='/vms/')
def submitlog(request):
    if request.method == 'POST':
        
        vehiclenumber = request.POST['vehiclenumber']
        drivername = request.POST['drivername']
        licensenumber=request.POST['licensenumber']
        gate = Gate.objects.get(gate_name=request.POST['gatenumber'])
        placetovisit = request.POST['placetovisit']
        purposeofvisit = request.POST['purposeofvisit']
        vehicletype = request.POST['vehicletype']
        vehiclemodel=request.POST['vehiclemodel']
        intime = datetime.now()
        log = VisitorLog(vehicle_number=vehiclenumber,driver_name=drivername,in_gate=gate,license_number=licensenumber,place_to_visit=placetovisit,purpose_of_visit=purposeofvisit,in_time=intime, vehicle_type=vehicletype, vehicle_model=vehiclemodel)  
        log.save()
        messages.success(request, "Log successfully added")
        return render(request, 'security/enter_log.html',)

#def enterlog(request):
    
@login_required(login_url='/vms/')
def csventer(request):
    form =  DocumentForm()
    return render_to_response('list.html',
                 {'type':"type",'form': form  },context_instance=RequestContext(request))

@login_required(login_url='/vms/')
def updatelog(request):
    if request.method == 'POST':
        hello=VisitorLog.objects.get(id=request.POST['number'])
        gates = Gate.objects.all()
        #return HttpResponse("vehicle_number")
        return render_to_response('security/updatelog.html',{'log':hello,'gates':gates,},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("../log")

@login_required(login_url='/vms/')
def finallog(request):
    if request.method == 'POST':
        number=request.POST['number']
        outtime=datetime.now()
        log=VisitorLog.objects.get(id=number)
        log.out_time=datetime.now()
        gate = Gate.objects.get(gate_name=request.POST['gate'])
        log.out_gate=gate
        log.save()
        return HttpResponseRedirect("../log")
