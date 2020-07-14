from django.urls import path
from . import views
from . import cdn_views

app_name = 'parse'

urlpatterns = [
    # path('', views.home, name='home'),
    path('index/', cdn_views.index, name='index'),
    path('excel_to_csv/', views.excel_parse_to_csv),

    # path('model_form_upload/', views.model_form_upload, name='models_form_upload'),
    # path('linkupload/', cdn_views.linkUpload, name= "linkupload"),
    # path('resultshow/', cdn_views.excel_parse, name='result')
]
