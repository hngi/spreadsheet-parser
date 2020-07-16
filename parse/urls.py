from django.urls import path
from . import views
from . import cdn_views

app_name = 'parse'

urlpatterns = [
    path('', views.index, name='home'),
    #path('index/', cdn_views.cdn_parse, name='index'),
    path('excel_to_csv/', views.excel_parse_to_csv, name = "excel"),
    path('exceltopdf/', views.excel_to_pdf, name = "pdf"),

    path('upload/', views.form_upload, name='models_form_upload'),
    path('linkupload/', cdn_views.cdn_upload, name= "linkupload"),
   # path('resultshow/', cdn_views.excel_parse, name='result')
    path('', views.index, name='index'),
    path('json_parser/', views.excel_parse_to_json, name='json-parser'),
    path('', views.index, name='home'),
    path('index/', cdn_views.cdn_parse, name='index'),
    path('upload/', views.form_upload, name='models_form_upload'),
    path('linkupload/', cdn_views.cdn_upload, name= "linkupload"),
    # path('resultshow/', cdn_views.excel_parse, name='result')

]
