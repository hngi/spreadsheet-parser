from django.http import JsonResponse
from django.shortcuts import render
from .models import ExcelSaverModel
from django.http import JsonResponse
import pandas as pd
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import MDABudget, AdministrativeBudget
from .serializers import MDABudgetSerializer, MonthlySerializer
# imported serializers class MonthlySerializer from serializers.py 
from excel_parser.serializers import MonthlySerializer

media_url = settings.MEDIA_URL


# Create your views here.


class MonthlyView(viewsets.ModelViewSet):
    queryset = AdministrativeBudget.objects.all()  # this code is to call all object from the db
    serializer_class = MonthlySerializer  # this code use the class defined in the serializers.py


'''
added a C.B view for returning a list of all MDA transactions available in the database
assumed a serializer of name MDABudgetSerializer has already been made.
'''


class MDABudgetView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = MDABudget.objects.all()
    serializer_class = MDABudgetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


"""
A Views Function that extracts data from the database and store as a list of dictionaries, to make it easy to be
stored into the database. If you are to assigned to store in database please be aware that the file is stored in
'final_data' and the month is stored in 'month' . cheers from ferrum
"""


def administrative_budget(request):
    excel_files = request.FILES.getlist("excel_file")

    # a loop to get the files from the media folder
    for current_excel_file in excel_files:
        excel_file_name = current_excel_file.name
        current_file_path = f'media/monthly/{excel_file_name}'
        if os.path.exists(current_file_path):
            continue
        elif excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
            ExcelSaverModel.objects.get_or_create(monthly_file=current_excel_file)
            monthly_files_url = media_url + f'monthly/'

            # gets all files in Monthly folder
            for file in os.listdir(monthly_files_url):
                try:
                    absolute_file_path = monthly_files_url + f"/{file}"
                    # reading the excel file
                    df = pd.read_excel(absolute_file_path, usecols="B:G", encoding='utf-8')
                    # Dropping the unneccessary columns
                    data = df.dropna(axis=0, how="any")
                    data.columns = data.iloc[0]
                    data2 = data.iloc[1:, ].reindex()
                    # here is month, the variable in which the month is stored in
                    month = data2.columns[2]
                    data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
                    data2.columns = ["sector", "budget", "allocation", "total_allocation", "balance", "percentage"]
                    # we dont need percentage... dropping it
                    data2.drop(["percentage"], axis=1, inplace=True)

                    # formatting the floats to make sure they all have uniform decimal points
                    # initially they are returning floats in the form of exponentials.
                    data2["budget"] = data2["budget"].apply(lambda x: "{:.2f}".format(x))
                    data2["allocation"] = data2["allocation"].apply(lambda x: "{:.2f}".format(x))
                    data2["total_allocation"] = data2["total_allocation"].apply(lambda x: "{:.2f}".format(x))
                    data2["balance"] = data2["balance"].apply(lambda x: "{:.2f}".format(x))
                    # here is final_data, the list of dictionaries that can be easily stored in the database
                    final_data = data2.to_dict(orient="records")
                except KeyError:
                    continue
    return Response(status=status.HTTP_200_OK)
