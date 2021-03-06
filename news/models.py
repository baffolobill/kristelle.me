import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from nani.models import TranslatableModel, TranslatedFields,\
    TranslationManager


class PublicNewsManager(models.Manager):
    def get_query_set(self):
        return super(PublicNewsManager, self).get_query_set()\
            .filter(published=True,
                    pub_date__lte=datetime.datetime.now())


class News(TranslatableModel):
    published = models.BooleanField(_('Published'), default=False)
    pub_date = models.DateTimeField(_('Publication date'), 
                                    default=datetime.datetime.now())
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    translations = TranslatedFields(
        title = models.CharField(_('Title'), max_length=255),
        content = models.TextField(_('Content')),
        )

    public = PublicNewsManager()
    objects = TranslationManager()

    def __unicode__(self):
        return self.safe_translation_getter('title', unicode(_('No title')))


    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-pub_date',)
