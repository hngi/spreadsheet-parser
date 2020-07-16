import os
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from .forms import ExcelUploadForm
from excel_parser.settings import BASE_DIR
from .models import ExcelUpload
from .delete_script import clear_directory
from django.contrib import messages
from win32com import client
import win32api
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):
    excel_upload = ExcelUpload.objects.all()
    return render(request, 'landing_page.html', {'excel_upload': excel_upload})

def form_upload(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)

        # return render(request, 'file_upload.html',{'uploaded_file_url':uploaded_file_url})
    
    return render(request, 'file_upload.html')


def parse_excel_file(request):
    excel_file = request.FILES.get("file")
    excel_file_name = excel_file.name
    ExcelUpload.objects.save(document=excel_file)

    directory = os.path.join(BASE_DIR, 'media/user')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)
            try:
                df = pd.read_excel(f'{file_name}', usecols="B:G", encoding='utf-8')
                data = df.dropna(axis=0, how="any")
                data.columns = data.iloc[0]
                data2 = data.iloc[1:, ].reindex()
                nrows = 10
                data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
                data2.columns = ["sector", "budget", "allocation", "total_allocation", "balance", "percentage"]
                data2.drop(["percentage"], axis=1, inplace=True)
                final_data = data2.to_dict(orient="records")
                clear_directory()
                return render(request, 'result.html', {'final_data': final_data})

            except KeyError:
                messages.error(request, 'Error! Operation Failed.')
        else:
            messages.error(request, 'Error! No excel file found.')

@api_view(['POST', ])
def excel_parse_to_csv(request):
    file = request.FILES.get('file')
    filename = file.name
    ExcelUpload.objects.create(document=file)
    # file_path = request.data.get('file_path')
    # print(file_path, request.data)

    try:
        file_path = f'media/user/{filename}'
        # reading the excel file
        df = pd.read_excel(file_path, encoding='utf-8')
        os.remove(file_path)
        # Dropping the unnecessary columns
        data = df.dropna(axis=0, how="any")

        # here is month, the variable in which the month is stored in
        # month = data2.columns[2]
        data.columns = data.columns.map(lambda x: str(x))
        # data.columns = data.columns.map(lambda x: x.replace('\n', ''))

        # we don't need percentage, dropping it
        # data2.drop(["percentage"], axis=1, inplace=True)
        result = data.to_csv(index=False)
        return Response(result)

    except KeyError:
        messages.error(request, 'Error! Operation Failed.')

@api_view(['POST', ])
def excel_to_pdf(request):
    file = request.FILES.get('file')
    filename = file.name
    pdf_file_name = filename[-4:]
    ExcelUpload.objects.create(document=file)

    try:
        file_path = f'media/user/{filename}'
        pdfpath = f'media/user/{pdf_file_name}.pdf'
        app = client.DispatchEx("Excel.Application")
        app.Interactive = False
        app.visible = False
        Workbook = app.Workbooks.Open(file_path)
        converted_file = Workbook.ActiveSheet.ExportAsFixedFormat(0,pdfpath)
        Workbook.Close()

        return Response(request)

    except KeyError:
        messages.error(request, "Operation Failed")