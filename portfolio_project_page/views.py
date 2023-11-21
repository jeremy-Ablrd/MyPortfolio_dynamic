from django.conf import settings
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import Page
import os

# Create your views here.

def index(request):
    projects = Page.objects.all()
    return render(request, 'portfolio_project_page/index.html', {"projects": projects})

def page_generate(request, page_slug):
    contents = Page.objects.get(slug=page_slug)
    
    # instance_dl = contents.download_zip_images
    # path_access = str(instance_dl.path).split('/')    # url='folder/file.ext' and path='C://...folder/file.ext'
    # del path_access[-1]
    # page_folder = '/'.join(path_access) + instance_dl.url
    # image_files = []
    # for file in os.listdir(page_folder):
    #     if os.path.isfile(os.path.join(page_folder, file)):
    #         path = os.path.join(page_folder, file)
    #         image_files.append(path)
    
    return render(request, 'portfolio_project_page/template_projects.html', {"contents": contents, })   # "images": image_files (si download_image disponible)
    # raise ValidationError(f"{images_files}")

def data_frame(request):
    return render(request, 'portfolio_project_page/frame_contact.html')

# def energyreportcontain(request):
#     return render(request, 'portfolio_project_page/energy_report.html')