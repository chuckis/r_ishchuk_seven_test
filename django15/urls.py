from django.conf.urls import patterns, include, url
from django.contrib import admin
from django15.apps.note import views
from django15.apps.note.views import ListNoteView

admin.autodiscover()

urlpatterns = patterns('django15.apps.note.views',
        url(r'^$', ListNoteView.as_view(), name="note-list"),
        url(r'^page(?P<page>\d+)/$', ListNoteView.as_view()),
        url(r'add/', 'add'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
