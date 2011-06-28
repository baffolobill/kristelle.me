from django import template
from news import models

register = template.Library()

NEWS_SHOWED = 5

@register.inclusion_tag('news/html5_news.html', takes_context=True)
def html5_news_items(context):
    items = models.News.public.all()[:NEWS_SHOWED]
    context['items'] = []
    try:
        for item in items:
            if len(item.title) and len(item.content):
                context['items'].append(item)
    except:
        pass

    return context
