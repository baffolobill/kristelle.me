from django import template
from news import models

register = template.Library()

@register.inclusion_tag('news/html5_news.html', takes_context=True)
def html5_news_items(context):
    items = models.News.public.all()

    context['items'] = items
    return context
