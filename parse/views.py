from django.shortcuts import render, redirect
import pandas as pd
from .forms import ExcelUploadForm
from excel_parser.settings import BASE_DIR
from .models import ExcelUpload
import os

# Create your views here.


def home(request):
    excelupload = ExcelUpload.objects.all()
    return render(request, 'home.html', {'excelupload': excelupload})


def model_form_upload(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('home')
    else:
        form = ExcelUploadForm()
    return render(request, 'model_form_upload.html', {'form': form})


def parse_excel_file(request):
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
                print(final_data)
                return render(request, 'budget.html', {'final_data': final_data})

            except KeyError:
                print("failed")

        else:
            print('No excel file')
