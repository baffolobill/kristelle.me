import urllib
import urllib2

from django.utils import simplejson
from django import http, shortcuts
from django.template import RequestContext
from django.utils.translation import ugettext as _

FID = 40796308305

def fql(fql, args=None):
    if not args: 
        args = {}

    args["query"], args["format"] = fql, "json"

    file = urllib2.urlopen("https://api.facebook.com/method/fql.query?" + urllib.urlencode(args))
    try: 
        response = simplejson.loads(file.read())
    finally: 
        file.close()
        
    if type(response) == dict and response.get("error_code"):
        return (response, response["error_msg"], False)
    
    return (response, None, True)

def get_videos():
    query = "SELECT vid,title,description,"\
        " thumbnail_link, src"\
        " FROM video WHERE owner=%s"%FID
    
    return fql(query)

def index(request):
    items, errors, success = fql(query)
    
    ctx = RequestContext(request, {'videos':items,
                                   'errors': errors,
                                   'success': success})
    return shortcuts.render_to_response('videos/index.html', ctx)
index.navigation = _('videos')
