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
# router.register('mbabudget', views.MDABudgetView)
# router.register('economicrevenue', views.EconomicRevenueView)


urlpatterns = [
    path('', include(router.urls)),
    path('administrative_budget/', views.store_administrative_budget_values),
    path('administrative_budget/data/', views.AdministrativeView.as_view({'get': 'list'})),
    path('economic_revenue/data', views.stored_economic_revenue),
    path('economic_revenue/', views.store_economic_revenue_values),
    path('economic_expenditure/', views.store_economic_expenditure_values),
    path('economic_expenditure/data/', views.get_expenditure_values),
    path('government_functions/', views.store_government_functions_values),
    path('government_functions/data/', views.get_government_function),
    path('mda_budget/', views.store_mda_budget_values),
    path('mda_budget/data/', views.mda_budget_view),
]
