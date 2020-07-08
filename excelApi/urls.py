from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 


urlpatterns = [
path('', views.index, name='index'),
path('budget.html', views.budget, name='budget'),
  
]