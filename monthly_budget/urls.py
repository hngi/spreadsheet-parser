from django.urls import path, include
from . import views
from rest_framework import routers

'''
This are the url paths leading to different end points. administrative, 
MBABudget and Economic i represented them as routers and i registered them into the 
routers and all routers are inclusive in the url path by including routers.urls
'''

router = routers.DefaultRouter()
# router.register('Monthlyadminsitrativebudget', views.AdministrativeView)
# router.register('administrative_budget/', views.store_administrative_budget_values)
# router.register('administrative_budget/data/', views.AdministrativeView.as_view({'get': 'list'}))
# router.register('mda_budget/', views.store_mda_budget_values)
# router.register('mda_budget/data/', views.get_mda_budget)
# router.register('economic_revenue/data', views.get_economic_revenue)
# router.register('economic_revenue/', views.store_economic_revenue_values)
# router.register('economic_expenditure/', views.store_economic_expenditure_values)
# router.register('economic_expenditure/data/', views.get_economic_expenditure)
# router.register('government_functions/', views.store_government_functions_values)
# router.register('government_functions/data/', views.get_government_function)
# router.register('mbabudget', views.MDABudgetView)
# router.register('economicrevenue', views.EconomicRevenueView)


urlpatterns = [
    path('administrative_budget/', views.store_administrative_budget_values),
    path('administrative_budget/data/', views.AdministrativeView.as_view({'get': 'list'})),
    path('mda_budget/', views.store_mda_budget_values),
    path('mda_budget/data/', views.get_mda_budget),
    path('economic_revenue/data', views.get_economic_revenue),
    path('economic_revenue/', views.store_economic_revenue_values),
    path('economic_expenditure/', views.store_economic_expenditure_values),
    path('economic_expenditure/data/', views.get_economic_expenditure),
    path('government_functions/', views.store_government_functions_values),
    path('government_functions/data/', views.get_government_function),
]
