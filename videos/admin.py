from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from videos import models
from nani.admin import TranslatableAdmin

class VideoAdmin(TranslatableAdmin):
    def queryset(self, request):
        language = self._language(request)
        return models.Video.objects.untranslated().all()

admin.site.register(models.Video, VideoAdmin)
