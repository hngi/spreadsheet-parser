from django.urls import path
from .views import ExcelAPIView,dailyAPIView


app_name = 'excelApi'


urlpatterns = [
    path('', ExcelAPIView.as_view(), name='post-parse'),
    path('daily/', dailyAPIView.as_view(), name='pre-parse'),

]
