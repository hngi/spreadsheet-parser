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
from pathlib import Path
<<<<<<< HEAD
=======
from .delete_script import clear_download


>>>>>>> 67a12b2c76e7076f7ffa0ab31ea81800dc38090a
# Create your views here.
#landing page view
def about(request):
    return render(request, "about_us.html")

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
<<<<<<< HEAD
        # return render(request, 'file_upload.html',{'uploaded_file_url':uploaded_file_url})
=======

>>>>>>> 67a12b2c76e7076f7ffa0ab31ea81800dc38090a
    elif request.method == "GET":
        return render(request, "file_upload.html")
# view for parsing the excel file into json and returning the file for download
def excel_parse_to_json(request):
    directory = os.path.join(BASE_DIR, r'media\upload')
<<<<<<< HEAD
=======
    filename = ""
>>>>>>> 67a12b2c76e7076f7ffa0ab31ea81800dc38090a
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
       # print(file)
        try:
            if filename.endswith('.xlsx'):
                file_name = os.path.join(directory, filename)
                df = pd.read_excel(file_name, encoding='utf-8')
                p= Path(file_name)
                realname = p.stem
                os.remove(file_name)
                data = df.dropna(axis=0, how='any')
                data.columns = data.columns.map(lambda x: str(x))
                data.columns = data.columns.map(lambda x: x.replace('\n', ''))
                final_data = data.to_dict(orient='records')
                path2 = f"media/user/{realname}.json"
                path3 =f"user/{realname}.json" 
                with open(path2, 'w') as fp:
                    json.dump(final_data, fp)
                filep = os.path.join(settings.MEDIA_ROOT, path3)
                if os.path.exists(filep):
                    
                    with open(filep,'rb') as fh:
                        response = HttpResponse(fh.read(), content_type='application/force-download')
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filep)
                    os.remove(filep)
                    return response
<<<<<<< HEAD
        else:
            error = 'Ooops!! An error occurred. Please input an excel file(.xlsx).'
            return render(request, 'file_upload.html', {'error':error})      
    except KeyError:
            error = 'Ooops!! Something went wrong in reading the contents of this excel file...'
            return render(request, 'file_upload.html', {'error':error})  
# view for parsing the excel file into csv and returning the file for download
=======
                                
            else:
                os.remove(f"media/upload/{filename}")
                error = 'Ooops!! An error occurred. Please input an excel file(.xlsx).  '
                return render(request, 'file_upload.html',{'error':error})     
        except KeyError:
                error = 'Ooops!! Something went wrong in reading the contents of this excel file...'
                return render(request, 'file_upload.html', {'error':error})  
    return redirect("parse:models_form_upload")


        # view for parsing the excel file into csv and returning the file for download
>>>>>>> 67a12b2c76e7076f7ffa0ab31ea81800dc38090a
def excel_parse_to_csv(request):
    directory = os.path.join(BASE_DIR, r'media\upload')
<<<<<<< HEAD
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
    try:
        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)
            file_path = f'media/upload/{filename}'
            df = pd.read_excel(file_path, encoding='utf-8')
            p= Path(file_path)
            realname = p.stem
            os.remove(file_path)
            data = df.dropna(axis=0, how="any")
            data.columns = data.columns.map(lambda x: str(x))
            path = f"media/user/{realname}.csv"
            data.to_csv(path, index=False)
            path3 =f"user/{realname}.csv"
            filep = os.path.join(settings.MEDIA_ROOT, path3)
            if os.path.exists(filep):
                with open(filep,'rb') as fh:
                    response = HttpResponse(fh.read(), content_type='application/force-download')
=======
    filename = ""
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        try:
            if filename.endswith('.xlsx'):
                file_name = os.path.join(directory, filename)
                file_path = f'media/upload/{filename}'
                df = pd.read_excel(file_path, encoding='utf-8')
                p= Path(file_path)
                realname = p.stem
                os.remove(file_path)
                data = df.dropna(axis=0, how="any")
                data.columns = data.columns.map(lambda x: str(x))
                path = f"media/user/{realname}.csv"
                data.to_csv(path, index=False)
                path3 =f"user/{realname}.csv"
                filep = os.path.join(settings.MEDIA_ROOT, path3)
                if os.path.exists(filep):
                    with open(filep,'rb') as fh:
                        response = HttpResponse(fh.read(), content_type='application/force-download')
>>>>>>> 67a12b2c76e7076f7ffa0ab31ea81800dc38090a
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filep)
                    os.remove(filep)
                    return response
<<<<<<< HEAD
        else:
            error = 'Ooops!! An error occurred. Please input an excel file(.xlsx).'
            return render(request, 'file_upload.html', {'error':error})      
    except KeyError:
            error = 'Ooops!! Something went wrong in reading the contents of this excel file...'
            return render(request, 'file_upload.html', {'error':error})  
    # except KeyError:
    #     messages.error(request, "Operation Failed")
=======
            else:
                os.remove(f"media/upload/{filename}")
                error = 'Ooops!! An error occurred. Please input an excel file(.xlsx).  '
                return render(request, 'file_upload.html',{'error':error})      
        except KeyError:
                error = 'Ooops!! Something went wrong in reading the contents of this excel file...'
                return render(request, 'file_upload.html', {'error':error})  
    return redirect("parse:models_form_upload")
    
>>>>>>> 67a12b2c76e7076f7ffa0ab31ea81800dc38090a






