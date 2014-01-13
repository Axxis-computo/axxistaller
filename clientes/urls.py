from django.conf.urls import patterns, url

from clientes import views

urlpatterns = patterns('',
  url(r'^$', views.cliente_list, name='cliente_list'),
  url(r'^new$', views.cliente_create, name='cliente_new'),
  url(r'^edit/(?P<pk>\d+)$', views.cliente_update, name='cliente_edit'),
  url(r'^delete/$', views.cliente_delete, name='cliente_delete'),
)