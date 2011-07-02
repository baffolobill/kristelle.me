from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    name = models.CharField(_('name'), max_length=255,
			    help_text=_('Not displayed, just for you.'))
    active = models.BooleanField(_('primary'), default=False)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
	
    class Meta:
        db_table = 'contacts_people'
	verbose_name = _('contact')
	verbose_name_plural = _('contacts')
	
    def __unicode__(self):
        return self.name
	
class PhoneNumber(models.Model):
    """Phone Number model."""
    person = models.ForeignKey(Person)
    phone_number = models.CharField(_('number'), max_length=50)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
    def __unicode__(self):
        return u"%s" % self.phone_number
	
    class Meta:
        db_table = 'contacts_phone_numbers'
	verbose_name = 'phone number'
	verbose_name_plural = 'phone numbers'
	    

class EmailAddress(models.Model):
    person = models.ForeignKey(Person)
	
    email_address = models.EmailField(_('email address'))
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_modified = models.DateTimeField(_('date modified'), auto_now=True)
    
    def __unicode__(self):
        return u"%s" % self.email_address
	
    class Meta:
        db_table = 'contacts_email_addresses'
	verbose_name = 'email address'
	verbose_name_plural = 'email addresses'

IM_SERVICE_CHOICES = (
    ('twitter', 'Twitter'),
    ('aim', 'AIM'),
    ('msn', 'MSN'),
    ('icq', 'ICQ'),
    ('jabber', 'Jabber'),
    ('yahoo', 'Yahoo'),
    ('skype', 'Skype'),
    ('qq', 'QQ'),
    ('sametime', 'Sametime'),
    ('gadu-gadu', 'Gadu-Gadu'),
    ('gtalk', 'Google Talk'),
    ('other', _('Other'))
)

class InstantMessenger(models.Model):
    person = models.ForeignKey(Person)	
    im_account = models.CharField(_('im account'), max_length=100)
    service = models.CharField(_('service'), max_length=11,
			       choices=IM_SERVICE_CHOICES, default='jabber')
    
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_modified = models.DateTimeField(_('date modified'), auto_now=True)
    
    def __unicode__(self):
        return u"%s" % self.im_account
	
    class Meta:
        db_table = 'contacts_instant_messengers'
	verbose_name = 'instant messenger'
	verbose_name_plural = 'instant messengers'

WEB_SERVICE_CHOICES = (
    ('website', _('Web Site')),
    ('facebook', _('Facebook.com')),
    ('vkontakte', _('Vkontakte.ru')),
    ('myspace', _('MySpace.com')),
)

class WebSite(models.Model):
    person = models.ForeignKey(Person)

    url = models.URLField(_('URL'))
    service = models.CharField(_('service'), max_length=11,
			       choices=WEB_SERVICE_CHOICES, default='website')
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
    def __unicode__(self):
        return u"%s" % self.url
	
    class Meta:
        db_table = 'contacts_web_sites'
	verbose_name = _('web site')
	verbose_name_plural = _('web sites')

