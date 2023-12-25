from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Home page</h1>")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services/services.html')
