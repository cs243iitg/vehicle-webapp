from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .forms import TheftForm
from .models import TheftReport


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