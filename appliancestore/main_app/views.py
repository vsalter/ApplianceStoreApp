from django.shortcuts import render
from django.http import HttpResponse
from .models import appliances



def home(request):
    return HttpResponse("<h1>Home page</h1>")

def about(request):
    return render(request, 'about.html')

def appliances_list(request):
    print(appliances)
    return render(request, 'appliances/appliances.html', {'appliances': appliances})
