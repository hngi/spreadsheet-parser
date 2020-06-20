from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register("budget", views.BudgetView)


urlpatterns = [
    path("", include(router.urls)),
]
