from django import forms
from .models import CDNUpload


# class LinkUploadForm(forms.ModelForm):
#     class Meta:
#         model = LinkUpload
#         fields = ('link', )


class CDNUploadForm(forms.Form):
    class Meta:
        model = CDNUpload
        link = forms.TextInput(
            attrs={
                    "position": "absolute;",
                    "width": "755px;",
                    "height": "68px;",
                    "left": "242px;",
                    "top": "554px;",
                    "background": "#FFFFFF;",
                    "border": "1px solid #828282;",
                    "box-sizing": "border-box;",
                    "border-radius": "5px;",
            }
        )
