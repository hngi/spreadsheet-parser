from django.urls import path
from .views import administativeBudgetView,mdaBudgetView,api_root
from rest_framework.urlpatterns import format_suffix_patterns


"""
Here is the urls that connects the views to the 
webpage and displays the right information 
and makes the journey through the api smooth. 
"""


urlpatterns = format_suffix_patterns([
    path('monthlyBudgetView',api_root),
    path('administrativeBudgetlist',administativeBudgetView.as_view({'get':'list'}),name='administrative-list'),
    path('mdaBudgetlist',mdaBudgetView.as_view({'get':'list'}),name='MDA-list'),
])
