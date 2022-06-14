import csv
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.files import File

from .models import FileModelConversion
from .forms import FileModelConversionForm
from .helper.helpers import file_handling_function



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
            #                                converted_file = converted_file)
        
            # instance.save()
            
            if file_type == 'CSV':

                converted_file = file_handling_function(file_name = file_name,
                                                    file_type = file_type,
                                                    file = uploaded_file)
                                                    
                response = HttpResponse(content_type='text/json')
                response['content-Disposition'] = 'attachment; filename=converted_format.json'

                response.write(converted_file)

                return response
            else: # i.e. if file_type == 'JSON'
                response = HttpResponse(content_type='text/csv')
                response['content-Disposition'] = 'attachment; filename=converted_format.csv'

                writer = csv.writer(response)

                # Repair the below :-
                for i in uploaded_file.read().decode('utf-8').splitlines():
                    writer.writerow(i)
            
                return response
            # HttpResponse(converted_file, content_type='text/plain')
            #print(converted_file)
            

            #Thereafter, we can see what to do..
            # form = FileModelConversionForm()
            # return render(request, 'file_converter_app/file_converter.html', {'form': form})
    else:
        form = FileModelConversionForm()
    return render(request, 'file_converter_app/file_converter.html', {'form': form})