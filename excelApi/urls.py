from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('result', views.excel_parse, name='parse'),
    path('upload', views.link_upload, name='upload'),
]
