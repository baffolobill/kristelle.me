from django import template
from news import models

register = template.Library()

NEWS_SHOWED = 5

@register.inclusion_tag('news/html5_news.html', takes_context=True)
def html5_news_items(context):
    context['items'] = models.News.public.all()[:NEWS_SHOWED]

    return context
