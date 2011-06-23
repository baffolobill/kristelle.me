from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext

from biography.forms import BiographyForm
from biography.models import Biography

from nani.admin import TranslatableAdmin
    
class BiographyAdmin(TranslatableAdmin):
    """ Admin for news """

    list_display = ('name', 'active')
    list_filter = ('active',)
    search_fields = ['name',]
    form = BiographyForm

    save_as = True
    save_on_top = True    

    #def queryset(self, request):
    #    """ Override to use the objects and not just the default visibles only. """
    #    language = self._language(request)
    #    return News.objects.language(language).all()

    def save_model(self, request, obj, form, change):
        if obj.active:
            Biography.objects.filter(active=True).update(active=False)
	obj.save()


admin.site.register(Biography, BiographyAdmin)
