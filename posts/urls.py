from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.apost, name='apost'),
)
