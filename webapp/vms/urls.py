from django.conf.urls import url
from vms import views

urlpatterns = [
    url(r'^$', views.login),
    url('auth/$', views.auth_view),
    url('logout/$', views.logout),
    url('home/$', views.home),
    url('invalid/$', views.login),

    url('report-theft/$', views.report_theft),
    url('submit-theft-report/$', views.report_theft),
    url('your-theft-reports/$', views.user_theft_reports),
    url(r'^(?P<theft_report_id>\d+)/cancel-theft-report/$',
        views.cancel_theft_report),


    #Section: Added by Karthik -> during integration with the website
    #Users urls
    url('users/dashboard/$', views.home),
    url('users/parking/$', views.parking_availability),
    url('users/register-vehicle/$', views.register_vehicle),
    url('users/suspicious/$', views.suspicious_vehicles),
    url('users/theft/$', views.report_theft),
    #Admin urls
    url('admin/dashboard/$', views.admin_home),
    url('admin/bus_timing/$', views.admin_bustiming),
    url('admin/passes/$', views.admin_passes),
    url('admin/theft/$', views.report_theft),
    url('admin/logs', views.admin_logs),
    url('admin/suspicious_display', views.admin_suspicious_display),
    url('admin/register-vehicle', views.register_vehicle),
    url('admin/registered-vehicles', views.admin_registered_vehicles),
    #EndSection

    url('register-vehicle/$', views.register_vehicle),
    url('submit-vehicle-registration/$', views.register_vehicle),
    url('your-vehicle-registrations/$', views.user_vehicle_registrations),
    url(r'^(?P<student_vehicle_id>\d+)/cancel-vehicle-registration/$',
        views.cancel_student_vehicle_registration),
]
