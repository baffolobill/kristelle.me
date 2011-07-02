from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from filebrowser.fields import FileBrowseField
from nani.models import TranslatableModel, TranslatedFields, TranslationManager
from nani.manager import TranslationFallbackManager

class PhotoAlbum(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('album title'), max_length=255),
        description = models.TextField(_('description'), blank=True),
        )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    ordering = models.IntegerField(_('ordering'), max_length=11, blank=True, null=True)
    published = models.BooleanField(_('published'), default=False)

    objects = TranslationManager()
    fallback = TranslationFallbackManager()

    def __unicode__(self):
        return self.safe_translation_getter('title', _('No title'))

    @models.permalink
    def get_absolute_url(self):
        return ('photos.views.album', [self.pk,])

    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.ordering is None:
            try:
                last = model.objects.order_by('-ordering')[0]
                self.ordering = last.ordering + 1
            except IndexError:
                self.ordering = 0

        return super(PhotoAlbum, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('photo album')
        verbose_name_plural = _('photo albums')
        ordering = ('ordering',)

class Photo(models.Model):
    album = models.ForeignKey(PhotoAlbum)
    file = FileBrowseField(_('image'), max_length=255, directory='photo',
                           extensions=['.png','.jpg'])
    ordering = models.IntegerField(_('ordering'), max_length=11, blank=True, null=True)
    published = models.BooleanField(_('published'), default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.file.filename

    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.ordering is None:
            try:
                last = model.objects.order_by('-ordering')[0]
                self.ordering = last.ordering + 1
            except IndexError:
                self.ordering = 0

        return super(Photo, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')
        ordering = ('ordering',)
