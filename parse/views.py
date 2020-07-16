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
<<<<<<< HEAD
import json
=======
>>>>>>> 87e4fdf6109634bf0a04b1597181cbe8ca11f91a


# Create your views here.


def index(request):
<<<<<<< HEAD
  #  excel_upload = ExcelUpload.objects.all()
    return render(request, 'landing_page.html')
=======
    pass
    return render(request, 'index.html')


# def home(request):
#     excel_upload = ExcelUpload.objects.all()
#     return render(request, 'excel.html', {'excel_upload': excel_upload})

>>>>>>> 87e4fdf6109634bf0a04b1597181cbe8ca11f91a

def form_upload(request):

    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
<<<<<<< HEAD
        return redirect("parse:excel")

        # return render(request, 'file_upload.html',{'uploaded_file_url':uploaded_file_url})
    elif request.method == "GET":
        return render(request, "file_upload.html")
    


# def parse_excel_file(request):
#     # excel_file = request.FILES.get("myfile")
#     # print(excel_file)
#     # excel_file_name = excel_file.name
#     # ExcelUpload.objects.save(document=excel_file)
#     directory = os.path.join(BASE_DIR, 'media/')
#     for file in os.listdir(directory):
#         filename = os.fsdecode(file)
#         if filename.endswith('.xlsx'):
#             file_name = os.path.join(directory, filename)
#             try:
#                 df = pd.read_excel(f'{file_name}', usecols="B:G", encoding='utf-8')
                
#                 data = df.dropna(axis=0, how="any")
#                 data.columns = data.iloc[0]
#                 data2 = data.iloc[1:, ].reindex()
#                 nrows = 10
#                 data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
#                 data2.columns = ["sector", "budget", "allocation", "total_allocation", "balance", "percentage"]
#                 data2.drop(["percentage"], axis=1, inplace=True)
#                 final_data = data2.to_dict(orient="records")
#                 clear_directory()
#                 return render(request, 'result.html', {'final_data': final_data})

#             except KeyError:
#                 messages.error(request, 'Error! Operation Failed.')
#         else:
#             messages.error(request, 'Error! No excel file found.')


def excel_parse_to_csv(request):
    # file = request.FILES.get('myfile')
    # print(file)
    # filename = file.name
    # ExcelUpload.objects.create(document=file)
    # file_path = request.data.get('file_path')
    # print(file_path, request.data)
    directory = os.path.join(BASE_DIR, 'media/')
=======
        print(uploaded_file_url)

        # return render(request, 'file_upload.html',{'uploaded_file_url':uploaded_file_url})
    return render(request, 'file_upload.html')


def excel_parse_to_json(request):
    directory = os.path.join(BASE_DIR, r'media\upload')

>>>>>>> 87e4fdf6109634bf0a04b1597181cbe8ca11f91a
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)
<<<<<<< HEAD
           
    try:
        #file_path = f'media/{file_name}'
        # reading the excel file
        df = pd.read_excel(file_name, encoding='utf-8')
        os.remove(file_name)
        

        # Dropping the unnecessary columns
=======
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
>>>>>>> 87e4fdf6109634bf0a04b1597181cbe8ca11f91a
        data = df.dropna(axis=0, how="any")
        data.columns = data.columns.map(lambda x: str(x))
<<<<<<< HEAD
        # data.columns = data.columns.map(lambda x: x.replace('\n', ''))

        # we don't need percentage, dropping it
        # data2.drop(["percentage"], axis=1, inplace=True)
        path = f"media/user/test.csv"
        path2 = f"media/user/test.json"
        result = data.to_csv(path, index=False)
        first_data = data.to_dict(orient = "records")
        with open(path2, 'w') as fp:
            json.dump(first_data,fp)
            context = {
                "path":path,
                "path2":path2
            }
        # file_path = file_name
        # pdfpath = 'media/user/test.pdf'
        # app = client.DispatchEx("Excel.Application")
        # app.Interactive = False
        # app.visible = False
        # Workbook = app.Workbooks.Open(file_path)
        # os.remove(file_name)
        # converted_file = Workbook.ActiveSheet.ExportAsFixedFormat(0,pdfpath)
        # Workbook.Close()
        print(path)
        return render(request, "download.html", {"path":path})
=======
        result = data.to_csv(index=False)
        return Response(result)
>>>>>>> 87e4fdf6109634bf0a04b1597181cbe8ca11f91a

    except KeyError:
        return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))


def excel_parse_to_pdf(request):
    directory = os.path.join(BASE_DIR, r'media\upload')

<<<<<<< HEAD

# def excel_to_pdf(request):
#     directory = os.path.join(BASE_DIR, 'media/')
#     for file in os.listdir(directory):
#         filename = os.fsdecode(file)
#         if filename.endswith('.xlsx'):
#             file_name = os.path.join(directory, filename)

#     try:
#         file_path = file_name
#         os.remove(file_name)
#         pdfpath = 'media/user/test.pdf'
#         app = client.DispatchEx("Excel.Application")
#         app.Interactive = False
#         app.visible = False
#         Workbook = app.Workbooks.Open(file_path)
#         converted_file = Workbook.ActiveSheet.ExportAsFixedFormat(0,pdfpath)
#         Workbook.Close()

#         return render(request, "download.html", {'file_path':file_path})

#     except KeyError:
#         messages.error(request, "Operation Failed")
=======
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
>>>>>>> 87e4fdf6109634bf0a04b1597181cbe8ca11f91a
