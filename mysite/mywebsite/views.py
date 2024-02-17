from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def interests(request):
    return render(request, 'interests.html')

def versailles(request):
    return render(request, 'versailles.html')

def contact(request):
    return render(request, 'contact.html')
# Create your views here.
