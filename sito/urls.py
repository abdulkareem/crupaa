from django.conf.urls import include, url
from django.contrib import admin

from sito import views
from sito.views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^language/(?P<language>[a-z\-]+)/$', language),
    url(r'^contact/$', contact, name='contact'),
    url(r'^success/$', success, name='success'),
]