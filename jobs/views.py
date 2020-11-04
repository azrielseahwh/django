from django.shortcuts import render, get_object_or_404
from .models import Job
import os
from os import listdir
from os.path import isfile, join

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def list_image_files():
    IMAGES_DIR = os.path.join(BASE_DIR, 'images')
    onlyfiles = [join("images", i) for i in listdir(IMAGES_DIR) if isfile(join(IMAGES_DIR, i))]
    return onlyfiles

def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs,'images':list_image_files})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})
