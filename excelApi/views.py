from django.shortcuts import render
import pandas as pd
from .forms import LinkUploadForm
from .models import LinkUpload

# Create your views here.


def index(request):
    linkupload = LinkUpload.objects.all()
    return render(request, 'index.html', {'linkupload': linkupload})


def link_upload(request):
    global file_name
    if request.method == 'POST':
        form = LinkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['link']
            for file in os.listdir(text):
                filename = os.fsencode(file)
                if filename.endswith('.xlsx'):
                    file_name = os.path.join(text, filename)
            # form.save()

    else:
        form = LinkUploadForm()
    return render(request, 'model_form_upload.html', {'form': form})


def budget(request):
    try:
        # reading the excel file
        df = pd.read_excel(f'{file_name}', usecols="B:G", encoding='utf-8')

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
        return render(request, 'budget.html', {'final_data': final_data})

    except KeyError:
        print("failed")
