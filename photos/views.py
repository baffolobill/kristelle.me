from django.utils import simplejson
from django import http, shortcuts
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from photos import models

class JSONResponse(http.HttpResponse):
    def __init__(self, data, **kwargs):
        defaults = {
            'content_type': 'application/json',
            }
        defaults.update(kwargs)
        super(JSONResponse, self).__init__(simplejson.dumps(data), defaults)


def get_albums():
    items = models.PhotoAlbum.fallback.filter(published=True)

    return (items, None, True)

def album(request, album_id):
    try:
        album = models.PhotoAlbum.fallback.get(published=True,
                                               pk=album_id)
    except Exception, e:
        return JSONResponse({'error':str(e)})

    images = models.Photo.objects.filter(published=True, album=album)

    ctx = RequestContext(request, {'images':images,
                                   'album':album})

    html = render_to_string('photos/html5_album_photos.html', ctx)
    return JSONResponse({'html':html})


