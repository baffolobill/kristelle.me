from django.db import models
from django.utils.translation import ugettext as _


class Config4u(models.Model):
    name = models.CharField(_('name'), max_length=255,
			    help_text=_('Not displayed, just for you.'))
    facebook = models.CharField(_('facebook ID'), max_length=20)
    facebook_id = models.IntegerField(max_length=10, editable=False)
    vkontakte = models.IntegerField(_('vkontakte apiID'), max_length=11)
    show_news = models.IntegerField(_('displayed news'), max_length=2, default=5)

    active = models.BooleanField(_('primary'), default=False)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
	
    class Meta:
	verbose_name = _('settings')
	verbose_name_plural = _('settings')
	
    def __unicode__(self):
        return self.name

