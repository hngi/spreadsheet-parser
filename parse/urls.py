from django.urls import path
from . import views
from . import cdn_views

app_name = 'parse'

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='home'),
    #path('index/', cdn_views.cdn_parse, name='index'),
    path('excel_to_csv/', views.excel_parse_to_csv, name = "excel"),
    #path('exceltopdf/', views.excel_to_pdf, name = "pdf"),

    path('upload/', views.form_upload, name='models_form_upload'),
    path('linkupload/', cdn_views.cdn_upload, name= "linkupload"),
   # path('resultshow/', cdn_views.excel_parse, name='result')
=======
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('file_upload/', views.form_upload, name='file-upload'),
    path('json_parser/', views.excel_parse_to_csv, name='json-parser'),
    # path('exceltopdf/', views.excel_to_pdf),
=======
    path('', views.index, name='home'),
    path('index/', cdn_views.cdn_parse, name='index'),
    path('excel_to_csv/', views.excel_parse_to_csv),
    path('exceltopdf/', views.excel_to_pdf),
>>>>>>> eb5ee9342f942311a427e8f755c75cf846741241

    path('upload/', views.form_upload, name='models_form_upload'),
    path('linkupload/', cdn_views.cdn_upload, name= "linkupload"),
    # path('resultshow/', cdn_views.excel_parse, name='result')
>>>>>>> 87e4fdf6109634bf0a04b1597181cbe8ca11f91a
]
