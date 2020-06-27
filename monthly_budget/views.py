from django.http import JsonResponse
from django.shortcuts import render
from .models import ExcelSaverModelMonthly
from django.http import JsonResponse
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
import os
from django.conf import settings
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MDABudget, AdministrativeBudget, EconomicExpenditure
from .serializers import MDABudgetSerializer, AdministrativeExpensesSerializer, EconomicExpenditureSerializer
from rest_framework import viewsets
import xlrd


media_url = settings.MEDIA_URL

# Create your views here.

'''
This function is to call the data in the AdministrativeBudget models which is a table name in our db. it 
calls all object from the db under the name AdministrativeBudget and passes it on to the serializers class 
'''

class AdministrativeView(viewsets.ModelViewSet):
    queryset = AdministrativeBudget.objects.all()  # this code is to call all object from the db
    serializer_class = AdministrativeExpensesSerializer  # this code use the class defined in the serializers.py


@api_view(['POST', ])
def monthly_report(request):
    """
    A Views Function that extracts data from the database and store as a list of dictionaries, to make it easy to be stored into the database
    If you are to assigned to store in database
    please be aware that the file is stored in 'final_data' and the month is stored in 'month' . cheers from ferrum
    """
    excel_files = request.FILES.getlist("excel_file")

    # a loop to get the files from the media folder
    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name
        current_file_path = f'media/monthly/{excel_file_name}'
        if os.path.exists(current_file_path):
            continue
        elif excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthly.objects.get_or_create(monthly_file=current_excel_file)

        # gets all files in Monthly folder
            try:
                # reading the excel file
                df = pd.read_excel(current_file_path, usecols = "B:G",encoding='utf-8' )
                # removing excel file after its been read
                os.remove(current_file_path)
                # Dropping the unneccessary columns
                data = df.dropna(axis = 0, how= "any")
                data.columns = data.iloc[0]
                data2 = data.iloc[1:,].reindex()
                # here is month, the variable in which the month is stored in
                month = data2.columns[2]
                data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
                data2.columns = ["sector", "budget", "allocation","total_allocation","balance","percentage"]
                # we dont need percentage... dropping it
                data2.drop(["percentage"], axis = 1, inplace = True)
                # formatting the floats to make sure they all have uniform decimal points
                #initially they are returning floats in the form of exponentials.
                data2["budget"] = data2["budget"].apply(lambda x: "{:.2f}".format(x))
                data2["allocation"] = data2["allocation"].apply(lambda x: "{:.2f}".format(x))
                data2["total_allocation"] = data2["total_allocation"].apply(lambda x: "{:.2f}".format(x))
                data2["balance"] = data2["balance"].apply(lambda x: "{:.2f}".format(x))
                # here is final_data, the list of dictionaries that can be easily stored in the database
                final_data = data2.to_dict(orient = "records")

                # code to store into the DB goes here, data is in variable final_data
                for transaction in final_data:
                    AdministrativeBudget.objects.create(budget=budget,
                                        allocation=allocation,
                                        total_allocation=total_allocation,
                                        balance=balance)

            except KeyError:
                continue

    return Response(status=status.HTTP_200_OK)

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


'''
This function will extract the required economic expenditure data in the expenditure table to json, like this: 
 [{"name": "SALARY", "budget": 2454037551812.8213, "allocation": 217515280304.7, "total_allocation": 854641653160.53, 
 "balance": 1599395898652.2913}, {"name": "NON REGULAR ALLOWANCES", "budget": 1055706358677.2299, 
 "allocation": 66004017316.47, "total_allocation": 333894644535.48, "balance": 721811714141.7499}]
NB: I added json response on lines 155 and 175 for testing purposes. 
'''


@api_view(['POST'])
def get_expenditure_values(request):
    excel_files = request.FILES.getlist("excel_file")

    # a loop to get the files from the media folder
    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name
        current_file_path = f'media/monthly/{excel_file_name}'
        if os.path.exists(current_file_path):
            loc = current_file_path
            required_values = []
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            num_rows = sheet.nrows
            num_cols = sheet.ncols
            for i in range(num_rows):
                first_row_value = sheet.cell(i, 0).value
                if type(first_row_value) == str:
                    type_of_data = "string"
                    # print(str(first_row_value) + ' is of type ' + type_of_data)
                    if first_row_value.replace('.', '', 1).isdigit():
                        new_first_row_value = int(first_row_value)
                        if new_first_row_value > 20000000:
                            row_check_value = new_first_row_value
                            row_data = {'name': sheet.cell(i, 1).value, 'budget': sheet.cell(i, 2).value,
                                        'allocation': sheet.cell(i, 3).value,
                                        'total_allocation': sheet.cell(i, 4).value,
                                        'balance': sheet.cell(i, 5).value}
                            # print(row_data)
                            required_values.append(row_data)
            # print(required_values)
            return JsonResponse(required_values, status=201, safe=False)
        elif excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthly.objects.get_or_create(monthly_file=current_excel_file)

            # if request.method == 'POST':
            loc = current_file_path
            required_values = []
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            num_rows = sheet.nrows
            num_cols = sheet.ncols
            for i in range(num_rows):
                first_row_value = sheet.cell(i, 0).value
                if type(first_row_value) == str:
                    type_of_data = "string"
                    # print(str(first_row_value) + ' is of type ' + type_of_data)
                    if first_row_value.replace('.', '', 1).isdigit():
                        new_first_row_value = int(first_row_value)
                        if new_first_row_value > 20000000:
                            row_check_value = new_first_row_value
                            row_data = {'name': sheet.cell(i, 1).value, 'budget': sheet.cell(i, 2).value,
                                        'allocation': sheet.cell(i, 3).value,
                                        'total_allocation': sheet.cell(i, 4).value, 'balance': sheet.cell(i, 5).value}
                            # print(row_data)
                            required_values.append(row_data)
            # print(required_values)
            return JsonResponse(required_values, status=201, safe=False)
        else:
            break
