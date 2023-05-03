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
    instance_dl = contents.download_zip_images
    page_folder = instance_dl.path     # url='folder/file.ext' and path='C://...folder/file.ext'
    image_files = [f"{instance_dl.url}" + f"/{file}" for file in os.listdir(page_folder) if os.path.isfile(os.path.join(page_folder, file))]
    return render(request, 'portfolio_project_page/template_projects.html', {"contents": contents, "images": image_files})
    # raise ValidationError(f"{images_files}")

def data_frame(request):
    return render(request, 'portfolio_project_page/frame_contact.html')

# def energyreportcontain(request):
#     return render(request, 'portfolio_project_page/energy_report.html')