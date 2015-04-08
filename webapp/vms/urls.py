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

    url('register-vehicle/$', views.register_vehicle),
    url('submit-vehicle-registration/$', views.register_vehicle),
    url('your-vehicle-registrations/$', views.user_vehicle_registrations),
    url(r'^(?P<student_vehicle_id>\d+)/cancel-vehicle-registration/$',
        views.cancel_student_vehicle_registration),
]
