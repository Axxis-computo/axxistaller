from django.conf.urls import patterns, url

urlpatterns = patterns('home.views',
  url(r'^$','home_view',name='Home_view'),
  url(r'^logout/$','logout_view',name='logout_view'),
)