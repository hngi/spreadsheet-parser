from django.shortcuts import render
import pandas as pd
import json
from .models import Budget
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Budget
from .serializers import Rend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


@api_view(['GET','POST'])
def budget_view(request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    if request.method == 'GET':
        budget = Budget.objects.all()
        context = paginator.paginate_queryset(budget, request)
        serializer = Rend(context, many = True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == "POST":
        serializer = Rend(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)



# Create your views here.


def budget(request):
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
    data2.drop(["total_allocation"], axis=1, inplace=True)
    final_data = data2.to_dict(orient="records")

    for index in range(len(final_data)):
        for each_data in final_data[index]:
    
            budget = Budget()
            budget.MDA_name = final_data[index]['sector']
            budget.project_recipient_name = final_data[index]['budget']
            budget.project_name = final_data[index]['allocation']
            budget.project_amount = final_data[index]['balance']
            # budget.project_date = each_data['project_date']
            budget.save()
    return render(request, 'budget.html', {'final_data': final_data})



def index(request):
    name = " index"
    return render(request, 'index.html', {'name': name})
