import os
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
#from .cdn_forms import CDNUploadForm
#from .models import CDNUpload


def index(request):
    cdn_upload = CDNUpload.objects.all()
    return render(request, 'index.html', {'cdn_upload': cdn_upload})


def cdn_upload(request):
    global file_name
    if request.method == 'POST':
        form = CDNUploadForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['link']
            for file in os.listdir(text):
                filename = os.fsdecode(file)
                if filename.endswith('.xlsx'):
                    file_name = os.path.join(text, filename)
            # form.save()
    else:
        form = CDNUploadForm()
    return render(request, 'cdn_upload.html', {'form': form})


def cdn_parse(request):
    try:
        # reading the excel file
        df = pd.read_excel(file_name, usecols="B:G", encoding='utf-8')
        # Dropping the unnecessary columns
        data = df.dropna(axis=0, how="any")
        data.columns = data.iloc[0]
        data2 = data.iloc[1:, ].reindex()
        # data3 = df.book.nrows
        nrows = 10
        # here is month, the variable in which the month is stored in
        # month = data2.columns[2]
        data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
        data2.columns = ["sector", "budget", "allocation", "total_allocation", "balance", "percentage"]
        # we don't need percentage, dropping it
        data2.drop(["percentage"], axis=1, inplace=True)
        final_data = data2.to_dict(orient="records")
        return render(request, 'result.html', {'final_data': final_data})

    except KeyError:
        messages.error(request, 'Error! Operation Failed.')
