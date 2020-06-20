from django.shortcuts import render
from rest_framework import viewsets 
from .models import Budget
from .serializers import BudgetSerializer

class BudgetView(viewsets.ModelViewSet): 
	queryset = Budget.objects.all() # this code is to call all object from the db 
	serializer_class = BudgetSerializer # this code use the class defined in the serializers.py

# Create your views here.
