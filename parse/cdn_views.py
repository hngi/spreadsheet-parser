import os
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from excel_parser.settings import BASE_DIR
from django.contrib import messages
from django.conf import settings
import json
from pathlib import Path

#view for link upload

def cdn_upload(request):
    if request.method == 'POST':
        link = request.POST.get("link")
        p = Path(link)
        #getting the exact name
        realname = p.stem
        #if json button is clicked
        if 'jsonlink' in request.POST:
            #print(link)
            if link.endswith("xlsx"):
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
                    os.remove(filep)
                    return response
            elif link[-4:] != "xlsx":
                error = 'Invalid link, please input a direct link to the excelFile.'
                return render(request, 'cdn_upload.html', {'error':error}) 
           # return redirect("parse:index")
        # if csv button is clicked
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
                os.remove(filep)
                return response
            
    elif request.method =="GET":
        return render(request, 'cdn_upload.html')
