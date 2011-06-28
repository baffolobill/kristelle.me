from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kristelle_django.views.home', name='home'),
    # url(r'^kristelle_django/', include('kristelle_django.foo.urls')),

    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin_tools/', include('admin_tools.urls')),

#    url(r'^', include('news.urls')),

    url(r'^tinymce/', include('tinymce.urls')),

#    url(r'^photos/$', 'photos.views.index', {}, 'photos-index'),
    url(r'^photos/album/(?P<album_id>\d+)/$', 'photos.views.album', {}, 'photos-album'),


 #   url(r'^videos/$', 'videos.views.index', {}, 'videos-index'),
 #   url(r'^biography/$', 'biography.views.biography', {}, 'biography-index'),
 #   url(r'^contacts/$', 'contacts.views.detail', {}, 'contacts-detail'),

    url(r'^contact-us/$', 'contacts.views.contact_us', {}, 'contact-us'),
    url(r'^html5/$', 'django.views.generic.simple.direct_to_template', 
        {'template':'base.html'}, 'pages-root'),

    url(r'^music/album/(?P<album_id>\d+)/tracklist/$', 'music.views.album_tracks', {}, 'music-album-tracklist'),

    url(r'music/track/(?P<track_id>\d+)/download/$', 'music.views.send_track', {}, 'music-send-track'),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
