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
        raise Exception(str(response["error_code"]), response["error_msg"])
    
    return response

def index(request):
    query = "SELECT vid,title,description,"\
        " thumbnail_link, embed_html"\
        " FROM video WHERE owner=%s"%FID
    
    items = fql(query)
    
    ctx = RequestContext(request, {'videos':items})
    return shortcuts.render_to_response('videos/index.html', ctx)
index.navigation = _('videos')
