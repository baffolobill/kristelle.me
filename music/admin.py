from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from music import models

class TrackInline(admin.StackedInline):
    model = models.Track
    extra = 3
    fieldsets = (
        (None, {'fields': ('title', 'file', 'ordering'),}),
    )

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    list_filter = ('published',)
    inlines = [TrackInline,]


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'ordering')


admin.site.register(models.Album, AlbumAdmin)
admin.site.register(models.Track, TrackAdmin)
