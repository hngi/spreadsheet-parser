from django.shortcuts import render

# imported serializers class MonthlySerializer from serializers.py 
from excel_parser.serializers import MonthlySerializer

# Create your views here.
class MonthlyView(viewsets.ModelViewSet):
	queryset = AdministrativeBudget.objects.all() # this code is to call all object from the db
	serializer_class = MonthlySerializer # this code use the class defined in the serializers.py