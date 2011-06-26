from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from music import models
from photos.views import JSONResponse

def album_tracks(request, album_id):
    try:
        album = models.Album.objects.get(pk=album_id,published=True)
    except Exception, e:
        return JSONResponse({'error':_('Album does not exist.')})


    tracks = models.Track.objects.filter(album=album)
    if len(tracks) == 0:
        return JSONResponse({'error':_('Album has no tracks.')})

    ctx = RequestContext(request, {'album':album,
                                   'tracks':tracks})
    html = render_to_string('music/tracklist_ajax.html', ctx)
    return JSONResponse({'html':html})
