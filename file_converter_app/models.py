from django.db import models

# Create your models here.

class FileModelConversion(models.Model):

    file_type_choices = [
        ('csv', 'CSV'),
        ('json', 'JSON'),
    ]

    # Model Fields :
    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=4,choices=file_type_choices)
    file_description = models.TextField(default='Hey, I am the default description :)')
    uploaded_file = models.FileField(upload_to='csv_or_json/', max_length=150)
    converted_file = models.FileField(upload_to='json_or_csv/', max_length=150, default='csv_or_json/new_one.csv')
    
