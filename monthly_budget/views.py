from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import MDABudget, AdministrativeBudget
from .serializers import MDABudgetSerializer, MonthlySerializer


# Create your views here.


class MonthlyView(viewsets.ModelViewSet):
    queryset = AdministrativeBudget.objects.all()  # this code is to call all object from the db
    serializer_class = MonthlySerializer  # this code use the class defined in the serializers.py


'''
this function when called, takes json data in the format 
[{"mda":"Test","budget":100000,"allocation":27934783353.5,"total_allocation":686919637.6900000572,
"balance":2106428472.8900001049},{"mda":"Test","budget":100000,"allocation":27934783353.5,
"total_allocation":686919637.6900000572,"balance":2106428472.8900001049},
{"mda":"Test","budget":100000,"allocation":27934783353.5,"total_allocation":686919637.6900000572,
"balance":2106428472.8900001049}] and saves each of the rows to the database.
'''


def save_mda(json_data):
    length = len(json_data)
    for i in range(length):
        row = json_data[i]
        serializer = MDABudgetSerializer(data=row)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


'''
added a C.B view for returning a list of all MDA transactions available in the database
assumed a serializer of name MDABudgetSerializer has already been made.
'''


class MDABudgetView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = MDABudget.objects.all()
    serializer_class = MDABudgetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
