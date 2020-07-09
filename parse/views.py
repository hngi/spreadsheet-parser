from django.shortcuts import render, redirect
from .forms import ExcelUploadForm

# Create your views here.


def model_form_upload(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExcelUploadForm()
    return render(request, 'parse/model_form_upload.html', {'form': form})
