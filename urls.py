from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

from config4u.models import Config4u
c4u = Config4u.objects.filter(active=True)
vai = 10000000
if len(c4u):
    vai = c4u[0].vkontakte


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kristelle_django.views.home', name='home'),
    # url(r'^kristelle_django/', include('kristelle_django.foo.urls')),

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

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
