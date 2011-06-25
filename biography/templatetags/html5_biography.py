from django import template
from biography import models

register = template.Library()

@register.inclusion_tag('biography/html5_biography.html', takes_context=True)
def html5_biography_item(context):
    try:
        item = models.Biography.objects.filter(active=True)[0]
    except:
        item = None

    context['biography'] = item
    return context
