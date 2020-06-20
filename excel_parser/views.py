from django.shortcuts import render
from rest_framework import viewsets 
from .models import Budget
import pandas
import json
import numpy as np
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
from .models import ExcelSaverModel, Budget
from datetime import datetime
import os
from .serializers import BudgetSerializer

class BudgetView(viewsets.ModelViewSet): 
	queryset = Budget.objects.all() # this code is to call all object from the db 
	serializer_class = BudgetSerializer # this code use the class defined in the serializers.py

# get project media url
media_url = settings.MEDIA_URL

# this code block accepts several files at once or just one
# this only works for daily payment reports excel sheets

@api_view(['POST', 'GET'])
def daily_payment_report_view(request):
    # if to get all daily reports for one month, provide only year and month params
    # if to ge reports for a particular day, provide year, month and day params


    if request.method == 'POST':

        excel_files = request.FILES.getlist("excel_file")
        for current_excel_file in excel_files:
            excel_file_name = current_excel_file.name
            date = excel_file_name.split('-')
            day = date[0]
            month = date[1]
            year = date[2].split('.')[0]
            if len(year) < 3:
                year = '20' + year
            current_file_path = f'media/daily/{excel_file_name}'
            print(current_file_path)
            if os.path.exists(current_file_path):
                #  code to make sure all files are unique
                continue
            elif excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
                ExcelSaverModel.objects.get_or_create(daily_report_file=current_excel_file)
                daily_files_url = media_url + f'daily/'

                # gets all files in daily folder
                for daily_file in os.listdir(daily_files_url):
                    try:
                        required_file_path = daily_files_url + f'/{daily_file}'
                        data = pandas.read_excel(required_file_path, sheet_name=0, usecols='C:F')
                        data1 = data.dropna(axis=0, how='all', thresh=3)
                        data2 = data1.dropna(axis=1, how='all')
                        try:
                            data2.columns = data2.iloc[0]
                            if 'Description' in data2.columns:
                                data2 = data2.iloc[1:, ].reindex()

                            else:
                                data2.columns = data2.iloc[1]
                                data2 = data2.iloc[2:, ].reindex()
                        except IndexError:
                            continue

                        data2.columns = data2.columns.str.lower()
                        df = data2.rename(columns={'beneficiary name': 'project_recipient_name', 'amount': 'project_amount',
                                                    'description': 'project_description', 'organization name': 'organization_name'})

                        name = f'{day}-{month}-{year}'
                        date = datetime.strptime(name, '%d-%m-%Y').date()
                        df['project_date'] = date
                        print(data2[:6])
                        valid_data = ['JAN', 'FEB', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
                        pattern = ' 20|'.join(valid_data)
                        df['project_description'] = np.where(df['project_description'].str.contains(pattern, na=False),
                                                             df['project_description'].str[10:],
                                                             df['project_description'])
                        df['MDA_name'] = 'FEDERAL GOVERNMENT'
                        df['project_amount'] = df["project_amount"].apply(lambda x: {':.2f'}.format(x))

                        # store data in dict form. this is the data to loop over to store into db
                        daily_expenses = df.to_dict(orient='records')
                    except KeyError:
                        continue

                      # code to store into database...
                    for each_data in daily_expenses:
                        budget = Budget()
                        budget.MDA_name = each_data['MDA_name']
                        budget.project_recipient_name = each_data['project_recipient_name']
                        budget.project_name = each_data['organization_name']
                        budget.project_amount = each_data['project_amount']
                        budget.project_date = each_data['project_date']
                        budget.save()
                  

        return Response(status=status.HTTP_200_OK)
