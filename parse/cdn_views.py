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

def index(request):
  #  cdn_upload = CDNUpload.objects.all()
    return render(request, 'index.html', {'cdn_upload': cdn_upload})

def cdn_upload(request):
    if request.method == 'POST':
        link = request.POST.get("link")
        if 'jsonlink' in request.POST:
            df = pd.read_excel(link, encoding = 'uft-8')
            data = df.dropna(axis=0, how='any')
            data.columns = data.columns.map(lambda x: str(x))
            data.columns = data.columns.map(lambda x: x.replace('\n', ''))
            final_data = data.to_dict(orient='records')
            path2 = f"media/user/test.json"
            path3 =f"user/test.json" 
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
            path = f"media/user/test.csv"
            data.to_csv(path, index=False)
            path3 =f"user/test.csv"
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


# def cdn_upload(request):
#     global file_name
#     if request.method == 'POST':
#         form = CDNUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             text = form.cleaned_data['link']
#             for file in os.listdir(text):
#                 filename = os.fsdecode(file)
#                 if filename.endswith('.xlsx'):
#                     file_name = os.path.join(text, filename)
#             # form.save()
#     else:
#         form = CDNUploadForm()
    # return render(request, 'cdn_upload.html', {'form': form})


# def cdn_json_parse(request):
#     link = request.POST.get("link")
#     print(link)
#     try:
#         # reading the excel file
#         # df = pd.read_excel(file_name, usecols="B:G", encoding='utf-8')
#         # # Dropping the unnecessary columns
#         # data = df.dropna(axis=0, how="any")
#         # data.columns = data.iloc[0]
#         # data2 = data.iloc[1:, ].reindex()
#         # # data3 = df.book.nrows
#         # nrows = 10
#         # here is month, the variable in which the month is stored in
#         # month = data2.columns[2]
#         data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
#         data2.columns = ["sector", "budget", "allocation", "total_allocation", "balance", "percentage"]
#         # we don't need percentage, dropping it
#         data2.drop(["percentage"], axis=1, inplace=True)
#         final_data = data2.to_dict(orient="records")
#         return render(request, 'result.html', {'final_data': final_data})

#     except KeyError:
#         messages.error(request, 'Error! Operation Failed.')
