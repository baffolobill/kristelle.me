from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from config4u.models import Config4u
c4u = Config4u.objects.filter(active=True)
vai = 10000000
if len(c4u):
    vai = c4u[0].vkontakte


urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^photos/album/(?P<album_id>\d+)/$', 'photos.views.album', {}, 'photos-album'),

    url(r'^contact-us/$', 'contacts.views.contact_us', {}, 'contact-us'),
    url(r'^$', 'django.views.generic.simple.direct_to_template', 
        {'template':'base.html', 'vkontakte_apiId':vai}, 'pages-root'),

    url(r'^music/album/(?P<album_id>\d+)/tracklist/$', 'music.views.album_tracks', {}, 'music-album-tracklist'),

    url(r'music/track/(?P<track_id>\d+)/download/$', 'music.views.send_track', {}, 'music-send-track'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
