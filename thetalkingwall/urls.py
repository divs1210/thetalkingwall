from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^posts/', include('posts.urls', namespace="posts")),
    url(r'^admin/', include(admin.site.urls))
)
