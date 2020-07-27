from django.urls import path
from .views import ExcelAPIView,ExcelintroAPIView


app_name = 'excelApi'


urlpatterns = [
  #  path('', ExcelintroAPIView.as_view(), name='post-parse'),
    path('', ExcelAPIView.as_view(), name='pre-parse'),
    

]
