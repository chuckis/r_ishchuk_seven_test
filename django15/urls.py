from django.conf.urls import patterns, include, url
from django.contrib import admin
from note import views

admin.autodiscover()

urlpatterns = patterns('note.views',
        url(r'^$', 'index'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
