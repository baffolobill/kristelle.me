from django import template

register = template.Library()

@register.inclusion_tag('wall/html5_wall.html', takes_context=False)
def html5_wall_stuff():
    return {}
