from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register("home", views.BudgetView)
# router.register("daily-payment-report", views.daily_payment_report_view),
# router.register("daily_reports_view", views.get_daily_reports_view),


urlpatterns = [
    path("", include(router.urls)),
    path('daily-payment-report/', views.daily_payment_report_view),
    path('get_daily_reports_view/', views.get_daily_reports_view)
]
