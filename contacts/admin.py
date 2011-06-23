from django.contrib import admin
from contacts import models


class EmailAddressInline(admin.TabularInline):
    model = models.EmailAddress

class PhoneNumberInline(admin.TabularInline):
    model = models.PhoneNumber

class InstantMessengerInline(admin.TabularInline):
    model = models.InstantMessenger

class WebSiteInline(admin.TabularInline):
    model = models.WebSite

class PersonAdmin(admin.ModelAdmin):
    inlines = [
	    PhoneNumberInline,
	    EmailAddressInline,
	    InstantMessengerInline,
	    WebSiteInline,
	    ]
	
    list_display_links = ('name','active',)
    list_display = ('name', 'active',)
    list_filter = ('active',)

    def save_model(self, request, obj, form, change):
        if obj.active:
            models.Person.objects.filter(active=True).update(active=False)
	obj.save()

admin.site.register(models.Person, PersonAdmin)
