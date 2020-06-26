<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import MDABudget

class MDABudgetView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = MDABudget.objects.all()
    serializer_class = MDABudgetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

=======
from django.shortcuts import render

# imported serializers class MonthlySerializer from serializers.py 
from excel_parser.serializers import MonthlySerializer

# Create your views here.
class MonthlyView(viewsets.ModelViewSet):
	queryset = AdministrativeBudget.objects.all() # this code is to call all object from the db
	serializer_class = MonthlySerializer # this code use the class defined in the serializers.py
>>>>>>> f670f8e84fd42592f7fe709c228d8b7fd330ab42
