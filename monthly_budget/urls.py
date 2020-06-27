from django.urls import path, include
from . import views

urlpatterns = [
    path('daily-payment-report-monthly/', views.monthly_report),
]



