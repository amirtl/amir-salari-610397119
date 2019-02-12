from django import forms

class UploadFileForm(forms.Form):
    your_photo = forms.ImageField()


