from .models import ExcelSaverModelMonthlyEconomic, ExcelSaverModelMonthlyAdministrative, ExcelSaverModelMonthly, \
    EconomicRevenue, GovernmentFunctions
from django.http import JsonResponse
import pandas as pd
import os
from django.conf import settings
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MDABudget, AdministrativeBudget, EconomicExpenditure
from .serializers import MDABudgetSerializer, AdministrativeExpensesSerializer, EconomicExpenditureSerializer, \
    EconomicRevenueSerializer, GovernmentFunctionsSerializer
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


'''
added a C.B view for returning a list of all MDA transactions available in the database
assumed a serializer of name MDABudgetSerializer has already been made.
'''


@api_view(['GET'])
def mda_budget_view(request):
    if request.method == 'GET':
        qs = MDABudget.objects.all()
        serializer = MDABudgetSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({
        'status': 'failure',
        'data': {'message': 'Something went wrong'}
    })


'''
Added a view to export stored revenue data from DB, serializes and returns JSON output,
Serializer has been created, awaiting url. nifemi 
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


"""
This connects to the serializer of GovernmentFunctions, which converts the stored data in the DB to JSON when queried.
"""


@api_view(['GET', ])
def get_government_function(request):
    if request.method == 'GET':
        qs = GovernmentFunctions.objects.all()
        serializer = GovernmentFunctionsSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({
        'status': 'failure',
        'data': {'message': 'Something went wrong'}
    })


"""
A Views Function that extracts data from the administrative excel and store as a list of dictionaries, to make it easy to be
stored into the database. If you are to assigned to store in database please be aware that the file is stored in
'final_data' and the month is stored in 'month' . cheers from ferrum
"""


@api_view(['POST', ])
def administrative_budget(request):
    excel_files = request.FILES.getlist("excel_file")

    # a loop to get the files from the media folder
    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name
        current_file_path = f'media/monthly/Administrative/{excel_file_name}'

        if excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthlyAdministrative.objects.get_or_create(monthly_file=current_excel_file)
            try:
                # reading the excel file
                df = pd.read_excel(current_file_path, usecols="B:G", encoding='utf-8')
                # removing excel file after its been read
                os.remove(current_file_path)
                # Dropping the unnecessary columns
                data = df.dropna(axis=0, how="any")
                data.columns = data.iloc[0]
                data2 = data.iloc[1:, ].reindex()
                # here is month, the variable in which the month is stored in
                month = data2.columns[2].split()[0]

                data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
                data2.columns = ["sector", "budget", "allocation", "total_allocation", "balance", "percentage"]
                # we don't need percentage... dropping it
                data2.drop(["percentage"], axis=1, inplace=True)
                # formatting the floats to make sure they all have uniform decimal points
                # initially they are returning floats in the form of exponential.
                data2["budget"] = data2["budget"].apply(lambda x: "{:.2f}".format(x))
                data2["allocation"] = data2["allocation"].apply(lambda x: "{:.2f}".format(x))
                data2["total_allocation"] = data2["total_allocation"].apply(lambda x: "{:.2f}".format(x))
                data2["balance"] = data2["balance"].apply(lambda x: "{:.2f}".format(x))
                # here is final_data, the list of dictionaries that can be easily stored in the database
                final_data = data2.to_dict(orient="records")

                # code to store into the DB goes here, data is in variable final_data

                for transaction in final_data:
                    if not AdministrativeBudget.objects.filter(name=transaction['name'],
                                                               budget=transaction['budget'],
                                                               expenses=transaction['expenses'],
                                                               total_expenses=transaction['total_expenses'],
                                                               balance=transaction['balance'],
                                                               month=month).exists():
                        AdministrativeBudget.objects.create(name=transaction['name'],
                                                            budget=transaction['budget'],
                                                            expenses=transaction['expenses'],
                                                            total_expenses=transaction['total_expenses'],
                                                            balance=transaction['balance'],
                                                            month=month)
            except KeyError:
                continue

    return Response(status=status.HTTP_200_OK)


'''
This view function takes post request with key as excel_file and value as an upload excel file. It extracts the 
necessary MDA budget data from the file and saves it using the savemda() function above to the database. 
Data output format:
[{"mda": "LOSS ON INVENTORY", "budget": 2454037551812.8213, "allocation": 217515280304.7, 
"total_allocation": 854641653160.53, "balance": 1599395898652.2913}, {"mda": "IMPAIRMENT CHARGES - INVESTMENT PROPERTY 
- LAND & BUILDING - OFFICE", "budget": 1055706358677.2299, "allocation": 66004017316.47, 
"total_allocation": 333894644535.48, "balance": 721811714141.7499}]
NB: it returns the data saved to the database in Json Format, for testing purposes.
'''


@api_view(['POST'])
def get_mda_budget_values(request):
    excel_files = request.FILES.getlist("excel_file")

    # a loop to get the files from the media folder
    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name
        current_file_path = f'media/monthly/{excel_file_name}'
        if excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthly.objects.get_or_create(monthly_file=current_excel_file)
            loc = current_file_path
            required_values = []
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)

            os.remove(current_file_path)

            num_rows = sheet.nrows
            num_cols = sheet.ncols
            for i in range(num_rows):
                first_row_value = sheet.cell(i, 0).value
                if type(first_row_value) == str:
                    type_of_data = "string"
                    # print(str(first_row_value) + ' is of type ' + type_of_data)
                    if first_row_value.replace('.', '', 1).isdigit():
                        new_first_row_value = int(first_row_value)
                        if new_first_row_value < 100000000:
                            row_check_value = new_first_row_value
                            row_data = {'mda': sheet.cell(i, 1).value, 'budget': sheet.cell(i, 2).value,
                                        'allocation': sheet.cell(i, 3).value,
                                        'total_allocation': sheet.cell(i, 4).value,
                                        'balance': sheet.cell(i, 5).value}
                            # print(row_data)
                            required_values.append(row_data)
            # print(required_values)
            save_mda(required_values)
            return JsonResponse(required_values, status=201, safe=False)



'''
This is not a view function
It takes data extracted from MDA Budget excel sheet in the format below and saves them all to the database at once.
[{"mda": "LOSS ON INVENTORY", "budget": 2454037551812.8213, "allocation": 217515280304.7, 
"total_allocation": 854641653160.53, "balance": 1599395898652.2913}, {"mda": "IMPAIRMENT CHARGES - INVESTMENT PROPERTY 
- LAND & BUILDING - OFFICE", "budget": 1055706358677.2299, "allocation": 66004017316.47, 
"total_allocation": 333894644535.48, "balance": 721811714141.7499}]
'''


def save_mda(excel_output):
    arr = []
    for i in range(len(excel_output)):
        data = excel_output[i]
        if not MDABudget(
                mda=data['mda'],
                budget=data['budget'],
                allocation=data['allocation'],
                total_allocation=data['total_allocation'],
                balance=data['balance']
            ).exists():
            arr.append(
                MDABudget(
                    mda=data['mda'],
                    budget=data['budget'],
                    allocation=data['allocation'],
                    total_allocation=data['total_allocation'],
                    balance=data['balance']
                )
            )
    MDABudget.objects.bulk_create(arr)


'''
A view for the extraction of data from the excel file for the Economic revenue!
The extracted data is stored as a list of dictionary in a variable called economic_final_data  the month is stored in 
variable economic_month. And the data is parsed as follow:
name = name
revenue = MONTH -ACTUAL =N=
total_revenue = YEAR TO DATE
'''


@api_view(['POST', ])
def economic_revenue(request):
    excel_files = request.FILES.getlist("excel_file")

    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name
        current_file_path = f'media/monthly/Economic/{excel_file_name}'

        if excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthlyEconomic.objects.get_or_create(monthly_file=current_excel_file)
            try:
                # reading the excel file
                df = pd.read_excel(current_file_path, usecols="B:G", encoding='utf-8')

                # remove file after being read
                os.remove(current_file_path)
                print('done')
                # Dropping the unnecessary columns
                data = df.dropna(axis=0, how="any")
                data.columns = data.iloc[0]
                data2 = data.iloc[1:, ].reindex()
                # economic month, the variable in which the month is stored in, splitting to get the neccessary data
                economic_month = data2.columns[2]
                economic_month = economic_month.split()
                economic_month = economic_month[0]

                # replacing the break lines for easy parsing
                data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
                data2.columns = ["name", "budget", "revenue", "total_revenue", "balance", "percentage"]
                # dropping the columns that are not needed
                data2.drop(["percentage", "budget", "balance"], axis=1, inplace=True)

                # formatting the floats to make sure they all have uniform decimal points
                # initially they are returning floats in the form of exponentials.

                data2["revenue"] = data2["revenue"].apply(lambda x: "{:.2f}".format(x))
                data2["total_revenue"] = data2["total_revenue"].apply(lambda x: "{:.2f}".format(x))

                # here is final_data, the list of dictionaries that can be easily stored in the database
                economic_final_data = data2.to_dict(orient="records")

                """This code stores the returned data in the dictionary into the Table."""
                for revenues in economic_final_data:
                    if not EconomicRevenue.objects.filter(name=revenues['name'],
                                                          revenue=revenues['revenue'],
                                                          total_revenue=revenues['total_revenue'],
                                                          month=economic_month).exists():
                        EconomicRevenue.objects.create(name=revenues['name'],
                                                       revenue=revenues['revenue'],
                                                       total_revenue=revenues['total_revenue'],
                                                       month=economic_month)

            except KeyError:
                continue
    return Response(status=status.HTTP_200_OK)


@api_view(['POST', ])
def government_functions(request):
    excel_files = request.FILES.getlist("excel_file")

    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name
        current_file_path = f'media/monthly/Economic/{excel_file_name}'
        if excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthlyEconomic.objects.get_or_create(monthly_file=current_excel_file)
            try:
                # reading the excel file
                df = pd.read_excel(current_file_path, usecols="B:G", encoding='utf-8')

                # remove file after being read
                os.remove(current_file_path)

                # Dropping the unnecessary columns
                data = df.dropna(axis=0, how="any")
                data.columns = data.iloc[0]
                data2 = data.iloc[1:, ].reindex()


                data2.columns = ["name", "budget", "expenses", "total_expenses", "balance", "percentage"]
                data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
                print(data2.columns[3])
                month = data2.columns[3].split()[0]

                # dropping the columns that are not needed
                data2.drop(["percentage"], axis=1, inplace=True)

                # formatting the floats to make sure they all have uniform decimal points
                data2["expenses"] = data2["expenses"].apply(lambda x: "{:.2f}".format(x))
                data2["total_expenses"] = data2["total_expenses"].apply(lambda x: "{:.2f}".format(x))

                # here is final_data, the list of dictionaries that can be easily stored in the database
                final_data = data2.to_dict(orient="records")

                # The code to store into the db goes here using the final_data list
                for transaction in final_data:
                    if not GovernmentFunctions.objects.filter(code=transaction['code'],
                                                              name=transaction['name'],
                                                              expenses=transaction['expenses'],
                                                              total_expenses=transaction['total_expenses'],
                                                            balance=transaction['balance'],
                                                              month=month).exists():
                        GovernmentFunctions.objects.create(name=transaction['name'],
                                                           code=transaction['code'],
                                                           expenses=transaction['expenses'],
                                                           balance=transaction['balance'],
                                                           total_expenses=transaction['total_expenses'],
                                                           month=month)

            except KeyError:
                continue
    return Response(status=status.HTTP_200_OK)


'''
Added a view to export stored revenue data from DB, serializes and returns JSON output,
Serializer has been created, awaiting url. nifemi 
'''


@api_view(['GET'])
def stored_economic_revenue(request):
    if request.method == 'GET':
        qs = EconomicRevenue.objects.all()
        serializer = EconomicRevenueSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
        if excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModelMonthly.objects.get_or_create(monthly_file=current_excel_file)
            loc = current_file_path
            required_values = []
            wb = xlrd.open_workbook(loc)

            # delete file after it has been loaded
            os.remove(current_file_path)

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
                        if new_first_row_value < 20000000:
                            row_check_value = new_first_row_value
                            row_data = {'name': sheet.cell(i, 1).value, 'budget': sheet.cell(i, 2).value,
                                        'allocation': sheet.cell(i, 3).value,
                                        'total_allocation': sheet.cell(i, 4).value,
                                        'balance': sheet.cell(i, 5).value}

                            required_values.append(row_data)
            economic_expenditure_data(required_values)
            return JsonResponse(required_values, status=201, safe=False)


def economic_expenditure_data(current_excel_file):
    arr = []
    for i in range(len(current_excel_file)):
        data = current_excel_file[i]
        if not EconomicExpenditure(
                    name=data['name'],
                    budget=data['budget'],
                    allocation=data['allocation'],
                    total_allocation=data['total_allocation'],
                    balance=data['balance']
                ).exists():
            arr.append(
                EconomicExpenditure(
                    name=data['name'],
                    budget=data['budget'],
                    allocation=data['allocation'],
                    total_allocation=data['total_allocation'],
                    balance=data['balance']
                )
            )
    EconomicExpenditure.objects.bulk_create(arr)


