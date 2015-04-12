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
    DUMMY: Function to allow the administrator create/delete/update the passes issued
    """
    return render(request, 'admin/passes.html', {
        'username': request.user.username,
        'is_admin': True,
        })