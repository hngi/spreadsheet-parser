from django.shortcuts import render
from .models import ExcelSaverModel
import pandas as pd
import json
import os
from django.conf import settings
# imported serializers class MonthlySerializer from serializers.py 
from excel_parser.serializers import MonthlySerializer
media_url = settings.MEDIA_URL

# Create your views here.
class MonthlyView(viewsets.ModelViewSet):
	queryset = AdministrativeBudget.objects.all() # this code is to call all object from the db
	serializer_class = MonthlySerializer # this code use the class defined in the serializers.py




def monthly_report(request):
	excel_files = request.FILES.getlist("excel_file")
	for current_excel_file in excel_files:
		excel_file_name = current_excel_file.name
		current_file_path = f'media/monthly/{excel_file_name}'
		if os.path.exists(current_file_path):
			continue
		elif excel_file_name[-3:] == 'xls' or excel_file_name[-4:] == 'xlsx':
			ExcelSaverModel.objects.get_or_create(monthly_file=current_excel_file)
			monthly_files_url = media_url + f'daily/'

            # gets all files in Monthly folder
			for file in os.listdir(monthly_files_url):
				try:
					absolute_file_path = monthly_files_url +f"/{file}"
					df = pd.read_excel("Excel_files/MARCH.xlsx", usecols = "B:G",encoding='utf-8' )
					data = df.dropna(axis = 0, how= "any")
					data.columns = data.iloc[0]
					data2 = data.iloc[1:,].reindex()
					date = data2.columns[2]
					data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
					da = data2.rename(columns = {
							"Name":"sector",
							'BUDGET AMOUNT  ': "budget",
							"MARCH  " : "allocation",
							"YR PMTS TO DATE  " : "total_allocation",
							"BUDGET BALANCE  ": "balance"
							})
					#this one is joking with me
					#this is where oluwa ran mi lowo dey
					print(da.columns)
				except KeyError:
					continue


	
