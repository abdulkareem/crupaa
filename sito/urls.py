from django.conf.urls import include, url
from django.contrib import admin

from sito import views
from sito.views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^language/(?P<language>[a-z\-]+)/$', language),


]