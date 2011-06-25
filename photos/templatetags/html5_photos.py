from django import template
from photos import views

register = template.Library()

@register.inclusion_tag('photos/html5_albums.html', takes_context=True)
def html5_albums_items(context):
    items, errors, success = views.get_albums()
    
    context['albums'] = items
    context['errors'] = errors
    return context
