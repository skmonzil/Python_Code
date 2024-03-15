from django.shortcuts import render
from django .http import HttpResponse
from frist_app import views

# Create your views here.

def home(request):
    return render(request, 'frist_app/index.html')


