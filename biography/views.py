from django import http
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from biography import models

def biography(request):
    try:
        bla = models.Biography.objects.filter(active=True)[0]
    except:
        raise http.Http404

    return render_to_response('biography/index.html',
                              RequestContext(request, {'object':bla}))
biography.navigation = _('biography')

