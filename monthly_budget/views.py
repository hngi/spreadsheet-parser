from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import MDABudget
# imported serializers class MonthlySerializer from serializers.py
from excel_parser.serializers import MonthlySerializer

# Create your views here.
class MonthlyView(viewsets.ModelViewSet):
	queryset = AdministrativeBudget.objects.all() # this code is to call all object from the db
	serializer_class = MonthlySerializer # this code use the class defined in the serializers.py


'''
added a C.B view for returning a list of all MDA transactions available in the database
assumed a serializer of name MDABudgetSerializer has already been made.
'''
class MDABudgetView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = MDABudget.objects.all()
    serializer_class = MDABudgetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

