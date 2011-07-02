from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from videos import models
from nani.admin import TranslatableAdmin

class VideoAdmin(TranslatableAdmin):
    pass

admin.site.register(models.Video, VideoAdmin)
