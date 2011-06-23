from django.db import models
from django.utils.translation import ugettext as _
from filebrowser.fields import FileBrowseField

class Album(models.Model):
    title = models.CharField(_('album title'), max_length=255)
    #cover = models.ImageField(_('cover image'), upload_to='music/album/cover',
    #                          max_length=255)
    cover = FileBrowseField(_('cover'), max_length=255, directory='music/album/cover',
                            extensions=[".jpg", '.png'], blank=True, null=True)
    file = FileBrowseField(_('zip'), max_length=255, directory='music/album/zip',
                           extensions=['.zip',], blank=True, null=True,
                           help_text=_('zipped album'))
    ordering = models.IntegerField(_('ordering'), max_length=5, default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    published = models.BooleanField(_('published'), default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('album')
        verbose_name_plural = _('albums')

class Track(models.Model):
    album = models.ForeignKey(Album, null=True, blank=True)
    title = models.CharField(_('title'), max_length=255)
    #file = models.FileField(_('file'), upload_to='music/tracks', max_length=255)
    file = FileBrowseField(_('file'), max_length=255, directory='music/tracks',
                            extensions=['.mp3'])
    ordering = models.IntegerField(_('ordering'), max_length=5)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.ordering is None:
            try:
                last = model.objects.order_by('-ordering')[0]
                self.ordering = last.ordering + 1
            except IndexError:
                self.ordering = 0

        return super(Track, self).save(*args, **kwargs)
    class Meta:
        verbose_name = _('track')
        verbose_name_plural = _('tracks')
        ordering = ('ordering',)

