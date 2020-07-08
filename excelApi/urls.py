<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
>>>>>>> c35c04aa26cc8d6570dd2a9e8936dcd98f419868
from . import views


urlpatterns = [
    path('', views.budget, name='budget')
]
