import os
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from excel_parser.settings import BASE_DIR
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
from django.http import HttpResponse

# Create your views here.

#landing page view
def about(request):
    return render(request, "abous_us.html")
def index(request):
  #  excel_upload = ExcelUpload.objects.all()
    return render(request, 'landing_page.html')

#view for form upload, it collects the file from the form and save temporarily to media/upload
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

# view for parsing the excel file into json and returning the file for download
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
            path3 =f"user/test.json" 
            with open(path2, 'w') as fp:
                json.dump(final_data,fp)
            #return render(request, 'download.html', {'final_data': final_data})
            filep = os.path.join(settings.MEDIA_ROOT, path3)
            if os.path.exists(filep):
                with open(filep,'rb') as fh:
                    response = HttpResponse(fh.read(), content_type='application/force-download')
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filep)
                    return response
        else:
            return render(request, 'results.html', messages.error(request, 'Error! No excel file found.'))      
    except KeyError:
        return render(request, 'results.html', messages.error(request, 'Holloa! Something went wrong'))

# view for parsing the excel file into csv and returning the file for download
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
            data.to_csv(path, index=False)
            path3 =f"user/test.csv"
            filep = os.path.join(settings.MEDIA_ROOT, path3)
            if os.path.exists(filep):
                with open(filep,'rb') as fh:
                    response = HttpResponse(fh.read(), content_type='application/force-download')
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filep)
                    return response
        else:
            return render(request, 'file_upload.html', messages.error(request, 'Error! No excel file found.'))
        
    except KeyError:
        messages.error(request, "Operation Failed")


    # except KeyError:
    #     messages.error(request, "Operation Failed")
