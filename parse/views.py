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


# Create your views here.


def index(request):
    pass
    return render(request, 'index.html')


# def home(request):
#     excel_upload = ExcelUpload.objects.all()
#     return render(request, 'excel.html', {'excel_upload': excel_upload})


def form_upload(request):

    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)

        # return render(request, 'file_upload.html',{'uploaded_file_url':uploaded_file_url})
    return render(request, 'file_upload.html')


def excel_parse_to_json(request):
    directory = os.path.join(BASE_DIR, r'media\upload')

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)
            df = pd.read_excel(file_name, encoding='utf-8')
            data = df.dropna(axis=0, how='any')
            data.columns = data.columns.map(lambda x: str(x))
            data.columns = data.columns.map(lambda x: x.replace('\n', ''))
            final_data = data.to_dict(orient='records')
            return render(request, 'result.html', {'final_data': final_data})

        else:
            return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))


def excel_parse_to_csv(request):
    directory = os.path.join(BASE_DIR, r'media\upload')

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)

    try:
        file_path = f'media/upload/{filename}'
        df = pd.read_excel(file_path, encoding='utf-8')
        os.remove(file_path)
        data = df.dropna(axis=0, how="any")
        data.columns = data.columns.map(lambda x: str(x))
        result = data.to_csv(index=False)
        return Response(result)

    except KeyError:
        return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))


def excel_parse_to_pdf(request):
    directory = os.path.join(BASE_DIR, r'media\upload')

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)

    try:
        file_path = f'media/upload/{file_name}'
        pdf_path = f'media/upload/{file_name}.pdf'
        app = client.DispatchEx("Excel.Application")
        app.Interactive = False
        app.visible = False
        Workbook = app.Workbooks.Open(file_path)
        converted_file = Workbook.ActiveSheet.ExportAsFixedFormat(0, pdf_path)
        Workbook.Close()

        return Response(request)

    except KeyError:
        return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))
