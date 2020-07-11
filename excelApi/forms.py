from django import forms
from .models import LinkUpload


class LinkUploadForm(forms.ModelForm):
    class Meta:
        model = LinkUpload
        fields = ('document', )
