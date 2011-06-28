from django import template
from music import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

register = template.Library()

@register.inclusion_tag('music/html5_music.html', takes_context=True)
def html5_music_stuff(context):
    return context

@register.inclusion_tag('music/music_albums.html')
def music_albums():
    albums = models.Album.objects.filter(published=True).order_by('ordering')
    return {'albums':albums}

@register.inclusion_tag('music/music_album.html', takes_context=True)
def music_album(context, item):
    context['album'] = item
    return context

@register.inclusion_tag('music/single_tracks.html')
def single_tracks():
    tracks = models.Track.objects.filter(album__isnull=True).order_by('ordering')
    return {'tracks':tracks}

@register.inclusion_tag('music/single_track.html', takes_context=True)
def single_track(context, item):
    context['track'] = item
    return context
