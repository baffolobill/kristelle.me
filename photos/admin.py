from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from photos import models
from nani.admin import TranslatableAdmin

class PhotoInline(admin.StackedInline):
    model = models.Photo
    extra = 3
    fieldsets = (
        (None, {'fields': ('file', 'ordering', 'published')}),
        )

class PhotoAlbumAdmin(TranslatableAdmin):
    inlines = [PhotoInline,]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('file', 'ordering', 'published')

admin.site.register(models.PhotoAlbum, PhotoAlbumAdmin)
admin.site.register(models.Photo, PhotoAdmin)
