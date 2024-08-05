from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    is_id_column = forms.BooleanField(required=False, label="First column is ID/serial number")