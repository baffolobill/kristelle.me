from django.contrib import admin
from config4u import models
from facegraph import Graph

class Config4uAdmin(admin.ModelAdmin):	
    list_display_links = ('name','active',)
    list_display = ('name', 'facebook', 'vkontakte', 'show_news', 'active',)
    list_filter = ('active',)

    def save_model(self, request, obj, form, change):
        q = Graph()
        obj.facebook_id = q[obj.facebook]().id

        if obj.active:
            models.Config4u.objects.filter(active=True).update(active=False)
	obj.save()

admin.site.register(models.Config4u, Config4uAdmin)
