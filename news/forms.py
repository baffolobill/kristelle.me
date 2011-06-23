from django import forms
from django.conf import settings
from nani.forms import TranslatableModelForm
from news.models import News
from tinymce.widgets import TinyMCE

class NewsForm(TranslatableModelForm):
    class Meta:
        model = News
        
    def _get_widget(self):
        return TinyMCE()
        
        
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        widget = self._get_widget()
        self.fields['content'].widget = widget
