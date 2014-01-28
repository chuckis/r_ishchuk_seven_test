from django.conf.urls import patterns, include, url
from django.contrib import admin
from note import views
from note.views import ListNoteView

admin.autodiscover()

urlpatterns = patterns('note.views',
        url(r'^$', ListNoteView.as_view(), name="note-list"),
        url(r'^page(?P<page>\d+)/$', ListNoteView.as_view()),
        url(r'add/', 'add'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
