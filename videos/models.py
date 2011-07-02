from django.db import models
from django.utils.translation import ugettext_lazy as _
from nani.models import TranslatableModel, TranslatedFields, TranslationManager
from nani.manager import TranslationFallbackManager
from filebrowser.fields import FileBrowseField

class Video(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=255)
        )

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    ordering = models.IntegerField(_('ordering'), max_length=11, blank=True, null=True)
    published = models.BooleanField(_('published'), default=False)
    embed_html = models.TextField(_('embed html code'))
    preview = FileBrowseField(_('preview image'), max_length=255,
                              directory='videos/preview',
                              extensions=['.jpg','.jpeg','.png'], blank=True)

    fallback = TranslationFallbackManager()
    objects = TranslationManager()

    def __unicode__(self):
        return self.safe_translation_getter('title', unicode(_('No title')))

    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.ordering is None:
            try:
                last = model.fallback.order_by('-ordering')[0]
                self.ordering = last.ordering + 1
            except IndexError:
                self.ordering = 0

        return super(Video, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('video')
        verbose_name_plural = _('videos')
        ordering = ('ordering',)

