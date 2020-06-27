from django.urls import path, include
from . import views

from rest_framework import routers 

'''
This are the url paths leading to different end points. administrative, 
MBAbudget and Economic i represented them as routers and i registered them into the 
routers and all routers are inclusive in the url path by including routers.urls

'''
router = routers.DefaultRouter()
router.register('adminsitrativebudget', views.AdministrativeView)
router.register('mbabudget', views.MDABudgetView)
router.register('economicrevenue', views.EconomicRevenueView)

urlpatterns = [
	path('', include(router.urls)), 


    path('daily-payment-report-monthly/', views.monthly_report),
]



