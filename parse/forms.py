from django import forms
from .models import ExcelUpload
from .models import LinkUpload


class ExcelUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelUpload
        fields = ('document', )


class LinkUploadForm(forms.Form):
    widget=forms.TextInput(
        attrs={
                "position": "absolute;","width": "755px;",
                "height": "68px;",
                "left": "242px;",
                "top": "554px;",
                "background": "#FFFFFF;",
                "border": "1px solid #828282;",
                "box-sizing": "border-box;",
                "border-radius": "5px;",
        }
    )

