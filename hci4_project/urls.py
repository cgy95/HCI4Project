from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hci4_project.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/', include('registration.urls')),
    url(r'^visualisation/', include('visualisation.urls')),
)
