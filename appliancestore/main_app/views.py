from django.shortcuts import render
from django.http import HttpResponse
from .models import Appliance



def home(request):
    return HttpResponse("<h1>Home page</h1>")

def about(request):
    return render(request, 'about.html')

def appliances_list(request):
    appliances = Appliance.objects.all()
    return render(request, 'appliances/appliances.html', {'appliances': appliances})

def appliances_detail(request, appliance_id):
    appliance = Appliance.objects.get(id=appliance_id)
    return render(request, 'appliances/detail.html', {'appliance': appliance})
