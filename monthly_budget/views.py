from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MDABudget, AdministrativeBudget, EconomicExpenditure
from .serializers import MDABudgetSerializer, MonthlySerializer, EconomicExpenditureSerializer


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


'''
added a view for returning a list of all  Economic expenditures available in the database for each month
assumed a serializer of name EconomicExpenditureSerializer has already been made.
'''
@api_view(['GET', ])
def get_economic_expenditure(request):
    if request.method == 'GET':
        qs = EconomicExpenditure.objects.all()
        serializer = EconomicExpenditureSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({
                    'status': 'failure',
                    'data': {'message': 'Something went wrong'}
                })
