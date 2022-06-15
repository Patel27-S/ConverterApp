import csv
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.files import File

from .models import FileModelConversion
from .forms import FileModelConversionForm
from .helper.helper import file_handling_function



def upload_file(request):

    if request.method == 'POST':
        form = FileModelConversionForm(request.POST, request.FILES)

        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            file_type = form.cleaned_data['file_type']
            file_description = form.cleaned_data['file_description']
            uploaded_file = request.FILES['uploaded_file']

            # converted_file = file_handling_function(file_name = file_name,
            #                                         file_type = file_type,
            #                                         file = uploaded_file)

            # converted_file = File(converted_file)

            # instance = FileModelConversion(file_name = file_name,
            #                                file_type = file_type,
            #                                uploaded_file = uploaded_file,
            #                                file_description = file_description,
            #                                )
        
            # instance.save()
            
            if file_type == 'CSV':
                
                # json_string is returned by the below function
                converted_format = file_handling_function(
                                                    file_name = file_name,
                                                    file_type = file_type,
                                                    file = uploaded_file
                                                    )
                                                    
                response = HttpResponse(content_type='text/json')
                response['content-Disposition'] = 'attachment; filename=converted_format.json'

                response.write(converted_format)

                return response

            else: # i.e. if file_type == 'JSON'
                response = HttpResponse(content_type='text/csv')
                response['content-Disposition'] = 'attachment; filename=converted_format.csv'


                writer = csv.writer(response)

                # reading the json_data from file.
                json_data = uploaded_file.read().decode('utf-8')

                # Converting json_string into python data structure.
                json_data = json.loads(json_data)

                count = 0

                for data in json_data:
                    if count == 0:
                        header = data.keys()
                        writer.writerow(header)
                        count += 1
                    writer.writerow(data.values())

                return response

    else: 
        form = FileModelConversionForm()
    return render(request, 'file_converter_app/file_converter.html', {'form': form})