# Generated by Django 4.0.5 on 2022-06-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModelConversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('file_type', models.CharField(choices=[('csv', 'CSV'), ('json', 'JSON')], max_length=4)),
                ('uploaded_file', models.FileField(max_length=150, upload_to='csv_or_json/')),
            ],
        ),
    ]
