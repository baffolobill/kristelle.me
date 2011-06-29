import urllib
import urllib2

from facegraph import Graph

from django.utils import simplejson
from django import http, shortcuts
from django.template import RequestContext
from django.utils.translation import ugettext as _
from config4u.models import Config4u

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
    FID = '40796308305'

    config = Config4u.objects.filter(active=True)
    if len(config):
        FID = config[0].facebook_id

    query = "SELECT vid,title,description,"\
        " thumbnail_link, src"\
        " FROM video WHERE owner=%s"%FID
    
    return fql(query)


