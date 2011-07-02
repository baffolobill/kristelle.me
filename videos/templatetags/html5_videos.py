from django import template
from videos import views

register = template.Library()

@register.inclusion_tag('videos/html5_videos.html', takes_context=True)
def html5_videos_items(context):
    items = views.get_videos()

    context['videos'] = items

    return context
