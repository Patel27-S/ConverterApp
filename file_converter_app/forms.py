from django import forms
from .models import FileModelConversion


class FileModelConversionForm(forms.ModelForm):
    class Meta:
         model = FileModelConversion
         fields = ['file_name', 'file_type', 'file_description','uploaded_file']

         widgets = {
          'file_description': forms.Textarea(
                                            attrs={'rows':3, 'cols':25, 
                                            'placeholder':'Please enter the file description :)'}
                                            ),
                    }