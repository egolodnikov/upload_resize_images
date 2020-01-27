from django import forms


class UploadImageForm(forms.Form):
    url = forms.URLField(required=False)
    image = forms.ImageField(required=False)


class ImageDetailViewForm(forms.Form):
    width = forms.IntegerField()
    height = forms.IntegerField()
