from django.urls import path
from .views import ExcelAPIView


app_name = 'excelApi'


urlpatterns = [
    path('', ExcelAPIView.as_view(), name='post-parse'),
]
