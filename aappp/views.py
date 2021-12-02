from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   return HttpResponse('home')
def customer(request):
    return render(request,'home.html')    
