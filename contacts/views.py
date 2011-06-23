from django.core.urlresolvers import reverse
from django import http
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from contacts import models

def detail(request, template='contacts/detail.html'):
    try:
        person = models.Person.objects.filter(active=True)[0]
    except:
        raise http.Http404

    return render_to_response(template, RequestContext(request, {'object':person}))
detail.navigation = _('contacts')
