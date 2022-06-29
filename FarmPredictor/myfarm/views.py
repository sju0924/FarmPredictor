from django.shortcuts import render
import requests
# Create your views here.

def myfarm(request):        
    return render(request, 'myfarm/myfarm.html',{'page':{'title': '나의작물'}})

def select_crop(request):
    return render(request, 'myfarm/select_crop.html')