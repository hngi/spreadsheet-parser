from django import forms
from .models import ExcelUpload


class ExcelUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelUpload
        fields = ('document', )
