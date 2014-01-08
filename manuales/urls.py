from django.conf.urls import patterns, url

from manuales import views

urlpatterns = patterns('manuales.views',
  url(r'^$', 'manual_list', name='manual_list'),
  url(r'^new$', 'manual_create', name='manual_new'),
  url(r'^edit/(?P<pk>\d+)$', 'manual_update', name='manual_edit'),
  url(r'^delete/$', 'manual_delete', name='manual_delete'),
)