from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'axxistaller.views.home', name='home'),
    # url(r'^axxistaller/', include('axxistaller.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('home.urls')),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^problemas/', include('problemas.urls')),
)