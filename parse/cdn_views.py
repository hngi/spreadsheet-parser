import os
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .cdn_forms import CDNUploadForm
from .models import CDNUpload
from django.http import HttpResponse
from rest_framework.response import Response
from excel_parser.settings import BASE_DIR
from django.contrib import messages
from django.conf import settings
import json
from pathlib import Path

# def index(request):
#   #  cdn_upload = CDNUpload.objects.all()
#     return render(request, 'index.html', {'cdn_upload': cdn_upload})

def cdn_upload(request):
    if request.method == 'POST':
        link = request.POST.get("link")
        p = Path(link)
        realname = p.stem
        if 'jsonlink' in request.POST:
            df = pd.read_excel(link, encoding = 'uft-8')
            data = df.dropna(axis=0, how='any')
            data.columns = data.columns.map(lambda x: str(x))
            data.columns = data.columns.map(lambda x: x.replace('\n', ''))
            final_data = data.to_dict(orient='records')
            path2 = f"media/user/{realname}.json"
            path3 =f"user/{realname}.json" 
            with open(path2, 'w') as fp:
                json.dump(final_data,fp)
            filep = os.path.join(settings.MEDIA_ROOT, path3)
            if os.path.exists(filep):
                with open(filep,'rb') as fh:
                    response = HttpResponse(fh.read(), content_type='application/force-download')
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filep)
                    return response
                    return render(request, 'cdn_upload.html')
            else:
                return render(request, 'results.html', messages.error(request, 'Error! No excel file found.'))
           # return redirect("parse:index")
        elif "csvlink" in request.POST:
            df = pd.read_excel(link, encoding = 'uft-8')
            data = df.dropna(axis=0, how='any')
            data.columns = data.columns.map(lambda x: str(x))
            path = f"media/user/{realname}.csv"
            data.to_csv(path, index=False)
            path3 =f"user/{realname}.csv"
            filep = os.path.join(settings.MEDIA_ROOT, path3)
            if os.path.exists(filep):
                with open(filep,'rb') as fh:
                    response = HttpResponse(fh.read(), content_type='application/force-download')
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filep)
                    return response
                    
                    return render(request, 'cdn_upload.html')
            
            # return redirect("parse:")
        
    elif request.method =="GET":
        return render(request, 'cdn_upload.html')
