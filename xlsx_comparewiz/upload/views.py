from django.shortcuts import render, redirect
from upload.models import Document
from upload.forms import DocumentForm
from django.contrib.auth.decorators import login_required
import pandas as pd
# Create your views here.

@login_required(login_url='../login')
def home(request):
    documents = Document.objects.all()
    return render(request, 'upload/home.html', { 'documents': documents })


def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        # myfile = request.FILES['document']
        if form.is_valid():
            form.save()
            # df = pd.read_csv(myfile)
            # remove_duplicates(df)
            # return render(request, 'dropped_duplicates.html')
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload/form_upload.html', {
        'form': form
    })

def remove_duplicates(df):
    df = df.drop_duplicates(keep="first")
    data = df
    return data.to_csv('media/output/dropped_duplicates.csv')