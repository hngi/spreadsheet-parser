from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import pandas as pd 
import xlrd
import json
from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
#from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# df = pd.read_excel('./media/APRIL.xlsx')

# print(df.head())



def budget(request):

    try:
       
        # reading the excel file
        df = pd.read_excel('./media/APRIL.xlsx', usecols = "B:G",encoding='utf-8' )
        # Dropping the unneccessary columns
        data = df.dropna(axis = 0, how= "any")
        data.columns = data.iloc[0]
        data2 = data.iloc[1:,].reindex()    
        # data3 = df.book.nrows
        nrows = 10
     
        # here is month, the variable in which the month is stored in
        #month = data2.columns[2]
     
        data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
        data2.columns = ["sector", "budget", "allocation","total_allocation","balance","percentage"]
        # we dont need percentage... dropping it
        data2.drop(["percentage"], axis = 1, inplace = True)
     
     
        final_data = data2.to_dict(orient = "records")
        return render(request, 'budget.html', {'final_data': final_data})
       
        print(final_data)
    except KeyError:
        print("failed")

    
