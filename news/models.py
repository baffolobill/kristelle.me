import datetime

from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from nani.models import TranslatableModel, TranslatedFields,\
    TranslationManager


class PublicNewsManager(models.Manager):
    def get_query_set(self):
        return super(PublicNewsManager, self).get_query_set()\
            .filter(published=True,
                    pub_date__lte=datetime.datetime.now())


class News(TranslatableModel):
    slug = models.SlugField(_('Slug'), unique_for_date='pub_date',
                            help_text=_('A slug is a short name which uniquely identifies the news item for this day'))
    published = models.BooleanField(_('Published'), default=False)
    pub_date = models.DateTimeField(_('Publication date'), 
                                    default=datetime.datetime.now())
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    translations = TranslatedFields(
        title = models.CharField(_('Title'), max_length=255),
        excerpt = models.TextField(_('Excerpt'), blank=True),
        content = models.TextField(_('Content'), blank=True),
        )

    public = PublicNewsManager()
    objects = TranslationManager()

    def __unicode__(self):
        return self.safe_translation_getter('title', self.slug)

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {
                'year': self.pub_date.strftime("%Y"),
                'month': self.pub_date.strftime("%m"),
                'day': self.pub_date.strftime("%d"),
                'slug': self.slug})

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-pub_date',)
