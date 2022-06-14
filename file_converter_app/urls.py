from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('upload_content/', views.upload_file)
]