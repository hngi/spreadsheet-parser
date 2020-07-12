import os
import pandas as pd
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import LinkUploadForm


# Create your views here.
@api_view(['POST'])
def link_upload(request):
    global file_name
    if request.method == 'POST':
        form = LinkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['link']
            for file in os.listdir(text):
                filename = os.fsdecode(file)
                if filename.endswith('.xlsx'):
                    file_name = os.path.join(text, filename)
            # form.save()

    else:
        form = LinkUploadForm()
    return Response(form, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def excel_parse(request):
    file_path = request.POST.get('file_path')
    try:
        # reading the excel file
        df = pd.read_excel(file_path, encoding='utf-8')

        # Dropping the unnecessary columns
        data = df.dropna(axis=0, how="any")
        # data.columns = data.iloc[0]
        # data2 = data.iloc[1:, ].reindex()
        # data3 = df.book.nrows
        nrows = 10

        # here is month, the variable in which the month is stored in
        # month = data2.columns[2]
        data.columns = data.columns.map(lambda x: str(x))
        data.columns = data.columns.map(lambda x: x.replace('\n', ''))

        # we don't need percentage, dropping it
        # data2.drop(["percentage"], axis=1, inplace=True)
        final_data = data.to_dict(orient="records")
        return Response(final_data, status= status.HTTP_200_OK)

    except KeyError:
        messages.error(request, 'Error! Operation Failed.')

