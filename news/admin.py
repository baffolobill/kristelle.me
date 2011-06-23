from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext

from news.forms import NewsForm
from news.models import News

from nani.admin import TranslatableAdmin

    
class NewsAdmin(TranslatableAdmin):
    """ Admin for news """

    #date_hierarchy = 'pub_date'
    #list_display = ('slug', 'title', 'published', 'pub_date')
    #list_filter = ('published',)
    #search_fields = ['title', 'excerpt', 'content']
    form = NewsForm

    actions = ['make_published', 'make_unpublished']
    
    save_as = True
    save_on_top = True    

    def queryset(self, request):
        """ Override to use the objects and not just the default visibles only. """
        language = self._language(request)
        return News.objects.language(language).all()
    
    def make_published(self, request, queryset):
        """ Marks selected news items as published """
        rows_updated = queryset.update(published=True)
        self.message_user(request, ungettext('%(count)d newsitem was published', 
                                             '%(count)d newsitems where published', 
                                             rows_updated) % {'count': rows_updated})
    make_published.short_description = _('Publish selected news')

    def make_unpublished(self, request, queryset):
        """ Marks selected news items as unpublished """
        rows_updated =queryset.update(published=False)
        self.message_user(request, ungettext('%(count)d newsitem was unpublished', 
                                             '%(count)d newsitems where unpublished', 
                                             rows_updated) % {'count': rows_updated})
    make_unpublished.short_description = _('Unpublish selected news')

admin.site.register(News, NewsAdmin)
