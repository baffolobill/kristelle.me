from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()

@register.inclusion_tag('html5/footer.html', takes_context=True)
def footer_menu(context):
    items = [
        {'id': 'page-home',
        'title': _('News'),
        'label': _('News')},
        {'id': 'page-biography',
        'title': _('Biography'),
        'label': _('Biography')},
        {'id': 'page-music',
        'title': _('Music'),
        'label': _('Music')},
        {'id': 'page-videos',
        'title': _('Videos'),
        'label': _('Videos')},
        {'id': 'page-photos',
        'title': _('Photos'),
        'label': _('Photos')},
        {'id': 'page-wall',
        'title': _('Wall'),
        'label': _('Wall')},
        {'id': 'page-contacts',
        'title': _('Contact Us'),
        'label': _('Contact Us')},
        ]

    context['items'] = items

    return context
