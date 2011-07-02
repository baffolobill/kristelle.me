from django.contrib import admin
from config4u import models

class Config4uAdmin(admin.ModelAdmin):	
    list_display_links = ('name','active',)
    list_display = ('name', 'contactus_email', 'vkontakte', 'show_news', 'active',)
    list_filter = ('active',)

    def save_model(self, request, obj, form, change):
        if obj.active:
            models.Config4u.objects.filter(active=True).update(active=False)
	obj.save()

admin.site.register(models.Config4u, Config4uAdmin)
