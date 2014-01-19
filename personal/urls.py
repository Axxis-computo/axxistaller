from django.conf.urls import patterns, url

from personal import views

urlpatterns = patterns('',
  url(r'^$', views.staff_list, name='staff_list'),
  url(r'^my_profile/$', views.staff_profile, name='staff_profile')
)