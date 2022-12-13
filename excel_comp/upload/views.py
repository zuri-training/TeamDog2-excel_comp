from django.shortcuts import render, redirect
from upload.models import Document
from upload.forms import DocumentForm
# Create your views here.


def home(request):
    documents = Document.objects.all()
    return render(request, 'upload/home.html', { 'documents': documents })


def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload/form_upload.html', {
        'form': form
    })
