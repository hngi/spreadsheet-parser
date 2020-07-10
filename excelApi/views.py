from django.shortcuts import render
import pandas as pd
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def budget(request):
    try:
        # reading the excel file
        df = pd.read_excel('./media/APRIL.xlsx', usecols="B:G", encoding='utf-8')

        # Dropping the unnecessary columns
        data = df.dropna(axis=0, how="any")
        data.columns = data.iloc[0]
        data2 = data.iloc[1:, ].reindex()
        # data3 = df.book.nrows
        nrows = 10

        # here is month, the variable in which the month is stored in
        # month = data2.columns[2]
        data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
        data2.columns = ["sector", "budget", "allocation", "total_allocation", "balance", "percentage"]

        # we don't need percentage, dropping it
        data2.drop(["percentage"], axis=1, inplace=True)
        final_data = data2.to_dict(orient="records")
        return Response(final_data, status=status.HTTP_200_OK) #, 'budget.html', {'final_data': final_data})

    except KeyError:
        print("failed")


def index(request):
    name = " index"
    return render(request, 'index.html', {'name': name})