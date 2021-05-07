from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    #to get objects from db and turn them into python objects
    jobs = Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})