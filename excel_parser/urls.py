from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import (
   daily_payment_report_view,

)

router = routers.DefaultRouter()
router.register("budget", views.BudgetViewSet)


urlpatterns = [
    path("payment-report/", daily_payment_report_view),
    path("", include(router.urls)),

]
