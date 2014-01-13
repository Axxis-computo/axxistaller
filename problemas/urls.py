from django.conf.urls import patterns, url

from problemas import views

urlpatterns = patterns('',
  url(r'^$', views.problema_list, name='problema_list'),
  url(r'^new$', views.problema_create, name='problema_new'),
  url(r'^edit/(?P<pk>\d+)$', views.problema_update, name='problema_edit'),
  url(r'^delete/$', views.problema_delete, name='problema_delete'),
)