from django.urls import path, include
from . import views
from rest_framework import routers

'''
This are the url paths leading to different end points. administrative, 
MBABudget and Economic i represented them as routers and i registered them into the 
routers and all routers are inclusive in the url path by including routers.urls
'''

router = routers.DefaultRouter()
router.register('Monthlyadminsitrativebudget', views.AdministrativeView)
router.register('mbabudget', views.MDABudgetView)
router.register('economicrevenue', views.get_economic_revenue)
router.register('mda_budget', views.get_mda_budget)
router.register('economic_expenditure', views.get_economic_expenditure)
router.register('government_functions/', views.store_government_functions_values)
router.register('administrative_budget/data/', views.AdministrativeView.as_view({'get': 'list'})),
router.registerpath('economic_expenditure/data/', views.get_expenditure_data),
router.register('administrative_budget/', views.store_administrative_budget_values),


urlpatterns = [
    path('', include(router.urls)),

]
