from django.urls import path
from . import views
from . import cdn_views

app_name = 'parse'

urlpatterns = [
    path('', views.index, name='index'),
    path('file_upload/', views.form_upload, name='file-upload'),
    path('json_parser/', views.excel_parse_to_csv, name='json-parser'),
    # path('exceltopdf/', views.excel_to_pdf),

    # path('model_form_upload/', views.model_form_upload, name='models_form_upload'),
    # path('linkupload/', cdn_views.linkUpload, name= "linkupload"),
    # path('resultshow/', cdn_views.excel_parse, name='result')
]
