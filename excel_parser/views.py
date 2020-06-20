<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import viewsets 
from .models import Budget
from .serializers import BudgetSerializer

class BudgetView(viewsets.ModelViewSet): 
	queryset = Budget.objects.all() # this code is to call all object from the db 
	serializer_class = BudgetSerializer # this code use the class defined in the serializers.py

# Create your views here.
=======
import pandas
import json
import numpy as np
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError
from django.conf import settings
from .models import ExcelSaverModel
import os

# get project media url
media_url = settings.MEDIA_URL

# this code block assumes only one file is sent but can easily be refactored to work on several files
# this only works for daily payment reports excel sheets
# accepts a GET request with parameter daily-report = True, year, month and day to get all daily files for that day

@api_view(['POST', 'GET'])
def daily_payment_report_view(request):
    # if to get all daily reports for one month, provide only year and month params
    # if to ge reports for a particular day, provide year, month and day params


    if request.method == 'POST':
        try:
            excel_files = request.FILES.getlist("excel_file")
            for current_excel_file in excel_files:
                excel_file_name = current_excel_file.name
                date = excel_file_name.split('-')
                day = date[0]
                month = date[1]
                year = date[2].split('.')[0]
                current_file_path = f'media/daily/{year}/{month}/{day}/{excel_file_name}'

                if os.path.exists(current_file_path):
                    #  code to make sure all files are unique
                    continue
                elif excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
                    ExcelSaverModel.objects.create(daily_report_file=current_excel_file)
                    # more logic to validate stored files in db may be done here if necessary

                else:
                    #file extension not supported
                    # return Response(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
                    continue
            return Response(status=status.HTTP_200_OK)
        except MultiValueDictKeyError:
            # in case user uploaded more than one file
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET' and request.GET.get('daily-reports'):
        # variable that stores all sheet data in variable in python dict format
        # contains the data to be stored in the database

        year = request.GET.get('year')
        month = request.GET.get('month')

        daily_files_url = media_url + f'daily/'
        required_files_dir = daily_files_url + f'{year}/{month}'
        daily_expenses = {}

        # will be refactored into function soon
        if request.GET.get('day'):
            day = request.GET.get('day')
            file_dir = required_files_dir + f'/{day}'
            try:
                current_file_name = os.listdir(file_dir)[0]
                current_file = file_dir + f'/{current_file_name}'
            except FileNotFoundError:
                return Response(status=status.HTTP_404_NOT_FOUND)
            data = pandas.read_excel(current_file, sheet_name=0, usecols='C:F')
            data1 = data.dropna(axis=0, how='all', thresh=3)
            data2 = data1.dropna(axis=1, how='all')

            try:
                data2.columns = data2.iloc[0]

                if 'Description' in data2.columns:
                    pass
                else:
                    data2.columns = data2.iloc[1]
                data2 = data2.iloc[2:, ].reindex()
            except IndexError:
                return Response(status=status.HTTP_204_NO_CONTENT)

            df = data2.rename(columns={'Beneficiary Name': 'project_recipient_name', 'Amount': 'project_amount',
                                       'Description': 'project_description'})
            print(df[:5])
            df['project_date'] = df['project_description'].str[:8]
            valid_data = ['JAN', 'FEB', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
            pattern = ' 20|'.join(valid_data)
            df['project_date'] = np.where(df['project_description'].str.contains(pattern, na=False),
                                          df['project_description'].str[:8], '')
            df['project_description'] = np.where(df['project_description'].str.contains(pattern, na=False),
                                                 df['project_description'].str[10:],
                                                 df['project_description'])
            df['MDA_name'] = 'FEDERAL GOVERNMENT'
            df['project_date'] = df['project_date'].astype(str)
            value = str(current_file_name)

            # make dict identifier filename without its extension
            if 'xls' in current_file_name[-3:]:
                value = str(current_file_name)[:-4]
            if 'xlsx' in current_file_name[-4:]:
                value = str(current_file_name)[:-5]
            print(value)

            # store data in dict form
            daily_expenses[value] = df.to_dict(orient='records')
        else:
            # gets all files in daily folder
            for daily_file in os.listdir(required_files_dir) :
                current_file_dir = required_files_dir + f'/{daily_file}'
                current_file_name = os.listdir(current_file_dir)[0]
                current_file = current_file_dir + f'/{current_file_name}'
                data = pandas.read_excel(current_file, sheet_name=0, usecols='C:F')
                data1 = data.dropna(axis=0, how='all', thresh=3)
                data2 = data1.dropna(axis=1, how='all')

                try:
                    data2.columns = data2.iloc[0]

                    if 'Description' in data2.columns:
                        pass
                    else:
                        data2.columns = data2.iloc[1]
                    data2 = data2.iloc[2:, ].reindex()
                except IndexError:
                    return Response(status=status.HTTP_204_NO_CONTENT)

                df = data2.rename(columns={'Beneficiary Name': 'project_recipient_name', 'Amount':'project_amount', 'Description': 'project_description'})
                print(df[:5])
                df['project_date'] = df['project_description'].str[:8]
                valid_data = ['JAN', 'FEB', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
                pattern = ' 20|'.join(valid_data)
                df['project_date'] = np.where(df['project_description'].str.contains(pattern, na=False), df['project_description'].str[:8], '')
                df['project_description'] = np.where(df['project_description'].str.contains(pattern, na=False), df['project_description'].str[10:],
                                         df['project_description'])
                df['MDA_name'] = 'FEDERAL GOVERNMENT'
                df['project_date'] = df['project_date'].astype(str)
                value = str(daily_file)

                # make dict identifier filename without its extension
                if 'xls' in daily_file[-3:]:
                    value = str(daily_file)[:-4]
                if 'xlsx' in daily_file[-4:]:
                    value = str(daily_file)[:-5]
                print(value)
                # store data in dict form
                daily_expenses[value] = df.to_dict(orient='records')

        # variable containing data in json format
        json_data = json.dumps(daily_expenses)


        # for testing , return the data in Json format as response until db is made
        return Response(json_data, status=status.HTTP_200_OK)
>>>>>>> development
