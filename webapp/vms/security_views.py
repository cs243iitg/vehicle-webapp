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
from .models import TheftReport, StudentVehicle, BusTiming, PersonPass
from datetime import datetime

def log_form(request):
    pass

def log(request):
    """
    DUMMY: Function to add logs
    """

    return render(request, 'admin/logs.html', {
        'username': request.user.username,
        'is_admin': True,
        })

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

