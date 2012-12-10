from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from apps.views import *
from apps.file import upload_file

#from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
from settings import MEDIA_URL, MEDIA_ROOT, STATIC_ROOT
import logging

urlpatterns = patterns('',
    # Examples:
    url(r'^hello/$', hello),
    url(r'^file/$', upload_file),
    url(r'^all/$', view_all),
    url(r'^pic/(?P<pic_id>.*)$', view_picture),
    url(r'^f1/(?P<pic_id>.*)$', apply_filter_blur),
    url(r'^f2/(?P<pic_id>.*)$', apply_filter_contour),
    url(r'^f3/(?P<pic_id>.*)$', apply_filter_detail),
    url(r'^$', hello),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^statics/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':'/home/django-projects/picfilter/media'}),
   
)
logging.error( STATIC_ROOT)
logging.error( urlpatterns)
