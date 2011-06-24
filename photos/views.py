from facegraph import Graph
from django.utils import simplejson
from django import http, shortcuts
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

FID = 40796308305

class JSONResponse(http.HttpResponse):
    def __init__(self, data, **kwargs):
        defaults = {
            'content_type': 'application/json',
            }
        defaults.update(kwargs)
        super(JSONResponse, self).__init__(simplejson.dumps(data), defaults)


def get_albums():
    q = Graph()

    response = q[FID].albums()
    if type(response) == dict and response.get('error'):
        return (response, response['error']['message'], False)

    return (response.get('data', []), None, True)

def index(request):
    q = Graph()
    albums = q[FID].albums()['data']

    ctx = RequestContext(request, {'albums':albums})
    return shortcuts.render_to_response('photos/index.html', ctx)
index.navigation = _('photos')

def album(request, album_id):
    q = Graph()
    qa = q[album_id]
    album = qa()
    if type(album) == dict and album.get('error'):
        return JSONResponse({'error':album['error']['message']})

    images = qa.photos()
    if type(images) == dict and images.get('error'):
        return JSONResponse({'error':images['error']['message']})

    ctx = RequestContext(request, {'images':images['data'],
                                   'album':album})

    if request.GET.has_key('ajax'):
        html = render_to_string('photos/html5_album_photos.html', ctx)
        return JSONResponse({'html':html})
    else:
        return shortcuts.render_to_response('photos/album.html', ctx)
album.navigation = _('photos')
