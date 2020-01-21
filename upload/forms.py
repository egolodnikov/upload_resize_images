from django import forms


class UploadImageForm(forms.Form):
    url = forms.URLField(required=False)
    image = forms.ImageField(required=False)

