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
from .models import TheftReport, StudentVehicle, BusTiming, PersonPass, VisitorLog
from datetime import datetime
from .forms import DocumentForm

def log_form(request):
    return render_to_response('security/enter_log.html',
                 {'type':"type" },context_instance=RequestContext(request))

def log(request):
    return render_to_response('security/viewlog.html',
                 {'logs':VisitorLog.objects.all().order_by('-in_time') },context_instance=RequestContext(request))


    


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


def persondetails(request, pass_id):
    personpass=PersonPass.objects.get(id=pass_id)
    return render(request, 'security/person_pass.html',{
        'user':request.user,
        'passes':personpass,
        })

##Log enter view update
#def viewlog(request):
    
def submitlog(request):
    if request.method == 'POST':
        
        #gatenumber = request.POST['gatenumber']
        drivername = request.POST['drivername']
        licensenumber=request.POST['licensenumber']
        
        
        if 'licensenumber' in request.POST:
            licensenumber = request.POST['licensenumber']
        else:
            licensenumber = -4
        vehiclenumber = request.POST['vehiclenumber']
        gatenumber = request.POST['gatenumber']
        placetovisit = request.POST['placetovisit']
        purposeofvisit = request.POST['purposeofvisit']
        
        intime=datetime.now()
        log = VisitorLog(vehicle_number=vehiclenumber,driver_name=drivername,in_gate=gatenumber,license_number=licensenumber,place_to_visit=placetovisit,purpose_of_visit=purposeofvisit,in_time=intime)  
        log.save()
        return HttpResponseRedirect("../log")

#def enterlog(request):
    
def csventer(request):
    form =  DocumentForm()
    return render_to_response('list.html',
                 {'type':"type",'form': form  },context_instance=RequestContext(request))

def updatelog(request):
    if request.method == 'POST':
        hello=VisitorLog.objects.filter(vehicle_number=request.POST['number'])
        #return HttpResponse("vehicle_number")
        return render_to_response('security/updatelog.html',{'logs':hello},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("../log")
def finallog(request):
    if request.method == 'POST':
        number=request.POST['number']
        outtime=datetime.now()
        log=VisitorLog.objects.get(vehicle_number=number)
        log.out_time=datetime.now()
        log.out_gate=request.POST['gate']
        log.save()
        return HttpResponseRedirect("../viewlog")
