from django import http
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from contacts import models
from photos.views import JSONResponse

def detail(request, template='contacts/detail.html'):
    try:
        person = models.Person.objects.filter(active=True)[0]
    except:
        raise http.Http404

    return render_to_response(template, RequestContext(request, {'object':person}))
detail.navigation = _('contacts')

def contact_us(request):
    message = request.POST.get('message', '').strip()

    if len(message):
        try:
            send_mail(_('Feedback from kristelle.me'), 
                      message, 
                      settings.EMAIL_DONT_REPLY, 
                      [n[1] for n in settings.MANAGERS])
        except:
            return JSONResponse({'error':unicode(_('Sorry, cannot send email. Try again later.'))})

        return JSONResponse({'message':unicode(_('Thank you for contacting us.'))})
    else:
        return JSONResponse({'error':unicode(_('Thanks for empty message :)'))})
