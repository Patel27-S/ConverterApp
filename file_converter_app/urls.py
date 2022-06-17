from django.contrib import admin
from django.urls import path
from . import views

app_name = 'file_converter_app'

urlpatterns = [
    path('upload_content/', views.upload_file, name='upload_file'),
    path('files_list/', views.FileList.as_view(), name = 'files_list'),
    path('<int:id>/', views.download_file, name = 'download_file')
]