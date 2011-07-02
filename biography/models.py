from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from nani.models import TranslatableModel, TranslatedFields,\
    TranslationManager


class Biography(TranslatableModel):
    name = models.CharField(_('name'), max_length=255,
                            help_text=_('Not displayed, just for you.'))
    active = models.BooleanField(_('primary'), default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    translations = TranslatedFields(
        content = models.TextField(_('Content'), ),
        )

    objects = TranslationManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('biography')
        verbose_name_plural = _('biographies')
