"""
%% urls.py %%

This file is define the main url for the Software. It links the software with different applications.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::::::::::::#
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE URLS HERE::::::::::::::::::::::::::::::::::::#


urlpatterns = patterns('',
   
    (r'^$', direct_to_template,
                    { 'template': 'index.html' },),
    (r'^hello', direct_to_template,
                    { 'template': 'job_ok.html' }, ),
    (r'^tcc11_12/', include('Automation.tcc.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
   
   
)
