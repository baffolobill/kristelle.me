from django import template
from news import models
from config4u.models import Config4u

register = template.Library()

NEWS_SHOWED = 5

@register.inclusion_tag('news/html5_news.html', takes_context=True)
def html5_news_items(context):
    news_on_page = NEWS_SHOWED
    config = Config4u.objects.filter(active=True)
    if len(config) and config[0].show_news > 0:
        news_on_page = config[0].show_news

    items = models.News.public.all()[:news_on_page]
    context['items'] = []

    for item in items:
        try:
            if len(item.title) and len(item.content):
                context['items'].append(item)
        except:
            pass

    return context
