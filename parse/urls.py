from django.urls import path
from . import views
from . import cdn_views

app_name = 'parse'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('excel_to_csv/', views.excel_parse_to_csv, name = "excel"),
    path('upload/', views.form_upload, name='models_form_upload'),
    path('linkupload/', cdn_views.cdn_upload, name= "linkupload"),
    path('json_parser/', views.excel_parse_to_json, name='json-parser'),

  
]
