from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from vms import urls as vms_urls
from rest import urls as rest_urls
from webapp import settings



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vms/', include(vms_urls)),
    url(r'^rest/', include(rest_urls))

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
