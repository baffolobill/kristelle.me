from facegraph import Graph
from django.utils import simplejson
from django import http, shortcuts
from django.template import RequestContext
from django.utils.translation import ugettext as _

FID = 40796308305

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
    images = qa.photos()['data']
    
    ctx = RequestContext(request, {'images':images,
                                   'album':album})
    return shortcuts.render_to_response('photos/album.html', ctx)
album.navigation = _('photos')
