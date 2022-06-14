from django import forms
from .models import FileModelConversion


class FileModelConversionForm(forms.ModelForm):
    class Meta:
         model = FileModelConversion
         fields = ['file_name', 'file_type', 'file_description','uploaded_file']