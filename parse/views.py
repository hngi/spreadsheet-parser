import os
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from excel_parser.settings import BASE_DIR
from django.contrib import messages
from win32com import client
import win32api
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json


# Create your views here.


def index(request):
  #  excel_upload = ExcelUpload.objects.all()
    return render(request, 'landing_page.html')


def form_upload(request):

    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location = 'media/upload')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        if 'csv' in request.POST:
            return redirect("parse:excel")
            
        elif 'json' in request.POST:
            return redirect("parse:json-parser")

        # return render(request, 'file_upload.html',{'uploaded_file_url':uploaded_file_url})
    elif request.method == "GET":
        return render(request, "file_upload.html")


def excel_parse_to_json(request):
    # if request.POST.get('json'):
    directory = os.path.join(BASE_DIR, r'media\upload')

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
    try:
        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)
            df = pd.read_excel(file_name, encoding='utf-8')
            os.remove(file_name)
            data = df.dropna(axis=0, how='any')
            data.columns = data.columns.map(lambda x: str(x))
            data.columns = data.columns.map(lambda x: x.replace('\n', ''))
            final_data = data.to_dict(orient='records')
            path2 = f"media/user/test.json"
            with open(path2, 'w') as fp:
                json.dump(final_data,fp)
            return render(request, 'download.html', {'final_data': final_data})
        else:
            return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))
    except KeyError:
        return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))


def excel_parse_to_csv(request):
    # if request.POST.get('csv'):
    directory = os.path.join(BASE_DIR, r'media\upload')

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

    try:
        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)
            file_path = f'media/upload/{filename}'
            df = pd.read_excel(file_path, encoding='utf-8')
            os.remove(file_path)
            data = df.dropna(axis=0, how="any")
            data.columns = data.columns.map(lambda x: str(x))
            path = f"media/user/test.csv"
    
        
            result = data.to_csv(path, index=False)
            return render(request, "download.html", {"path":path})
        else:
            return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))
        
    except KeyError:
        return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))


def excel_to_pdf(request):
    directory = os.path.join(BASE_DIR, 'media/')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)

    try:
        file_path = file_name
        os.remove(file_name)
        pdfpath = 'media/user/test.pdf'
        app = client.DispatchEx("Excel.Application")
        app.Interactive = False
        app.visible = False
        Workbook = app.Workbooks.Open(file_path)
        converted_file = Workbook.ActiveSheet.ExportAsFixedFormat(0,pdfpath)
        Workbook.Close()

        return render(request, "download.html", {'file_path':file_path})

    except KeyError:
        messages.error(request, "Operation Failed")
