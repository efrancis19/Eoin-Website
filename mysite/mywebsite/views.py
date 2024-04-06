from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def hobbies(request):
    return render(request, 'hobbies.html')

def interests(request):
    return render(request, 'interests.html')

def contact(request):
    return render(request, 'contact.html')

def versailles(request):
    return render(request, 'versailles.html')

def new_file(request):
    return render(request, 'new_file.html')
# Create your views here.
