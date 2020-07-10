from django.urls import path
from . import views

app_name = 'parse'

urlpatterns = [
    path('', views.home, name='home'),
    path('model_form_upload/', views.model_form_upload, name='models_form_upload'),
]
