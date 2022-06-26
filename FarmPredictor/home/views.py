from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    if 'nickname' in request.session:
        nick = request.session['nickname']   
    else:
        nick = ""     
    return render(request, 'home/index.html',{'page':{'title':'홈'}, 'nickname':nick})