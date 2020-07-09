from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('budget', views.budget, name='budget'),
=======
    path('budget.html', views.budget, name='budget'),
>>>>>>> 091c9edcfed0f001d8a395b0faf565380d0540ac
]

