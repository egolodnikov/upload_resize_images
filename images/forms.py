from django import forms


class ImageDetailViewForm(forms.Form):
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
