from django import template
from contacts import models

register = template.Library()

@register.inclusion_tag('contacts/html5_contacts.html', takes_context=True)
def html5_contacts_stuff(context):
    try:
        person = models.Person.objects.filter(active=True)[0]
    except:
        person = None

    context['object'] = person
    
    return context
