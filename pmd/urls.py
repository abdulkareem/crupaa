#from django.conf.urls import include, url
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'pmd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('sito.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:  
        urlpatterns += patterns('',  
                                #REMOVE IT in production phase  
                                (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
                                {'document_root': settings.MEDIA_ROOT})
          )