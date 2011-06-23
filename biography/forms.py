from django import forms
from django.conf import settings
from nani.forms import TranslatableModelForm
from biography.models import Biography
from tinymce.widgets import TinyMCE

class BiographyForm(TranslatableModelForm):
    class Meta:
        model = Biography
        
    def _get_widget(self):
        return TinyMCE(attrs={'rows':20,'cols':80})
        
        
    def __init__(self, *args, **kwargs):
        super(BiographyForm, self).__init__(*args, **kwargs)
        widget = self._get_widget()
        self.fields['content'].widget = widget
