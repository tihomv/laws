from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from files.download import download_ipc
from files.read_python import read_pdf


def home(request):
    # file_name = download_ipc()
    # read_pdf(file_name)
    return render(request, 'court/home.html')
