from django.urls import path
from . import views


urlpatterns = [
    path('daily-payment-report/', views.daily_payment_report_view),
]