from django.conf.urls import url
from vms import views

urlpatterns = [
        url(r'^$', views.login),
        url('auth/$', views.auth_view),
        url('logout/$', views.logout),
        url('home/$', views.home),
        url('invalid/$', views.login),
]
