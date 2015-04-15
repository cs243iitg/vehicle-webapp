from django.conf.urls import url
from rest import views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    url(r'^api/$', views.test_view),
    url(r'^theft-report/$', views.theft_report),
    url(r'^suspicious-vehicle/$', views.suspicious_vehicle),
    url(r'^theft-report/(?P<pk>[0-9]+)$', views.theft_detail),
    url(r'^api-token-auth/', rest_views.obtain_auth_token),
    url(r'^parking-slot/$', views.parking_slot),
    url(r'^bus-timing/$', views.bus_timing)


]