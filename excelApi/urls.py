from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
path('', views.index, name='index'),
path('budget.html', views.budget, name='budget'),
  
]
=======
    path('', views.budget, name='budget')
]
>>>>>>> c35c04aa26cc8d6570dd2a9e8936dcd98f419868
