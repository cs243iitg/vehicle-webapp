from django.conf.urls import url
from vms import views, admin_views, security_views, users_views

urlpatterns = [
    url(r'^$', views.login),
    url('auth/$', views.auth_view),
    url('logout/$', views.logout),
    url('home/$', views.home),
    url('invalid/$', views.login),

    #Section: Added by Karthik -> during integration with the website
    
    #Common URLs for All
    url('dashboard/$',views.home),     #Users Dashboard will show his vehicles, Theft Reports Registered by him
    url('parking-slot-availability/$',views.parking_slot_availability),
    url('theft-report-form/$',views.theft_report_form),
    url('vehicles-missing/$',views.vehicles_missing),
    url('suspicious-vehicle-report-form/$', views.suspicious_vehicle_report_form),
    url('suspicious-vehicles/$', views.suspicious_vehicles),
    url('busdetails/$',views.busdetails),
    url(r'^suspicious-vehicles/delete/$', views.delete_suspicious_vehicles),
    url(r'^(?P<report_id>\d+)/download-theft-report/$', views.generate_report),    

    #Admin urls
    url('admin/guards-on-duty/$', admin_views.guards_on_duty),
    url('admin/parking-slot-update/$', admin_views.parking_slot_update),
    url('admin/upload-log/$', admin_views.upload_log),
    url('admin/vehicle-applications', admin_views.registered_vehicles),
    url('admin/registered-vehicles', admin_views.old_registered_vehicles),
    url('admin/add-guards', admin_views.add_guards),
    # url('admin/edit-user-details', admin_views.edit_user_details),
    url('admin/security',admin_views.security),
    # url('admin/admin-role',admin_views.admin_role),
    url('admin/update-bus-details',admin_views.update_bus_details),
    url('admin/block-passes',admin_views.block_passes), 
    url('admin/issue-pass',admin_views.issue_pass),
    url(r'^admin/empl/(?P<empl_vehicle_id>\d+)/process-vehicle-registration/$', admin_views.process_empl_vehicle_registration),
    url(r'^admin/stud/(?P<student_vehicle_id>\d+)/process-vehicle-registration/$', admin_views.process_stud_vehicle_registration),
    url(r'^admin/empl/(?P<vehicle_id>\d+)/approve-registration/$', admin_views.approve_reg),
    url(r'^admin/stud/(?P<vehicle_id>\d+)/approve-registration/$', admin_views.approve_reg),    
    url(r'^admin/empl/(?P<vehicle_id>\d+)/deny-registration/$', admin_views.deny_reg),
    url(r'^admin/stud/(?P<vehicle_id>\d+)/deny-registration/$', admin_views.deny_reg),    
    url('admin/add-place', admin_views.add_place),
    ######JAINAM#######
    # url('admin/guardcsv/$', admin_views.csventer),
    url('admin/viewcsv/$', admin_views.viewcsv),
    ###################

    
    #URLs Common for Users and Admin
    url('users/register-vehicle/$', users_views.register_vehicle),
    url('users/register-cycle/$', users_views.register_cycle),
    url('users/user_theft_reports', users_views.user_theft_reports),
    url(r'^users/(?P<theft_report_id>\d+)/cancel-theft-report/$', users_views.cancel_theft_report),
    url('users/your-vehicle-registrations/$', users_views.vehicle_registrations),    
    url(r'^users/(?P<student_vehicle_id>\d+)/cancel-vehicle-registration/$', users_views.cancel_vehicle_registration),
    url('users/register-vehicle/$', users_views.register_vehicle),
    url('users/submit-vehicle-registration/$', users_views.register_vehicle),
    url(r'^users/(?P<theft_report_id>\d+)/cancel-theft-report/$',users_views.cancel_theft_report),
    
    #Common URLs for Security and Admin
    url('security/log/$',security_views.log),
    url('security/log-form',security_views.log_form),
    url('security/updatelog/$',security_views.updatelog),       #jainam display log
    url('security/finallog/$',security_views.finallog),       #jainam display log
    url('security/submitlog/$',security_views.submitlog),       #jainam display log
    url('security/passes',security_views.passes), 
    url(r'^(?P<pass_id>\d+)/personpass/$',security_views.persondetails),     
    #EndSection


   
]
