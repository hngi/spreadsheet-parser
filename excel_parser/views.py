from rest_framework import viewsets
import pandas
import numpy as np
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
from .models import ExcelSaverModel, Budget
from datetime import datetime
import os
from django.db.models import Q
from .serializers import BudgetSerializer


class BudgetView(viewsets.ModelViewSet):
    queryset = Budget.objects.all()  # this code is to call all object from the db
    serializer_class = BudgetSerializer  # this code use the class defined in the serializers.py


# get project media url
media_url = settings.MEDIA_URL


# this code block accepts several files at once or just one
# this only works for daily payment reports excel sheets

@api_view(['POST'])
def store_daily_payments_data(request):
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
            if excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
                ExcelSaverModel.objects.get_or_create(daily_report_file=current_excel_file)
                # gets all files in daily folder
                try:
                    data = pandas.read_excel(current_file_path, sheet_name=0, usecols='C:F')
                    os.remove(current_file_path)
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
                    df = data2.rename(
                        columns={'beneficiary name': 'project_recipient_name', 'amount': 'project_amount',
                                 'description': 'project_description', 'organization name': 'organization_name'})

                    name = f'{day}-{month}-{year}'
                    date = datetime.strptime(name, '%d-%m-%Y').date()
                    df['project_date'] = date
                    valid_data = ['JAN', 'FEB', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
                    pattern = ' 20|'.join(valid_data)
                    df['project_description'] = np.where(df['project_description'].str.contains(pattern, na=False),
                                                         df['project_description'].str[10:],
                                                         df['project_description'])
                    df['MDA_name'] = 'FEDERAL GOVERNMENT'
                    df['project_amount'] = df['project_amount'].apply(lambda x: '{:.2f}'.format(x))

                    # store data in dict form. this is the data to loop over to store into db
                    daily_expenses = df.to_dict(orient='records')
                except KeyError:
                    continue

                # code to store into database...
                for transaction in daily_expenses:
                    if not Budget.objects.filter(MDA_name=transaction['MDA_name'],
                                                 project_recipient_name=transaction['project_recipient_name'],
                                                 project_name=transaction['organization_name'],
                                                 project_amount = transaction['project_amount'],
                                                 project_date=transaction['project_date']
                                                 ).exists():
                        budget = Budget()
                        budget.MDA_name = transaction['MDA_name']
                        budget.project_recipient_name = transaction['project_recipient_name']
                        budget.project_name = transaction['organization_name']
                        budget.project_amount = transaction['project_amount']
                        budget.project_date = transaction['project_date']
                        budget.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', ])
def get_daily_reports_view(request):
    if request.method == 'GET':
        day = request.GET.get('day')
        month = request.GET.get('month')
        year = request.GET.get('year')
        project_recipient_name = request.GET.get('project_recipient_name')
        qs = []

        if project_recipient_name and day and month and year:
            try:
                date_string = f'{day}-{month}-{year}'
                date = datetime.strptime(date_string, '%d-%m-%Y').date()
                qs = Budget.objects.filter(
                    Q(project_recipient_name__icontains=project_recipient_name) & Q(project_date=date)
                )
            except ValueError:
                return Response("'Wrong Date Format'")
        elif project_recipient_name:
            qs = Budget.objects.filter(project_recipient_name__icontains=project_recipient_name)
        elif day and month and year:
            try:
                date_string = f'{day}-{month}-{year}'
                date = datetime.strptime(date_string, '%d-%m-%Y').date()
                qs = Budget.objects.filter(project_date=date)
            except ValueError:
                return Response("Wrong Date Format")
        serializer = BudgetSerializer(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

