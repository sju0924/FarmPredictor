from django.shortcuts import render, redirect
import requests
import os
from rest_framework.decorators import api_view, permission_classes
from dotenv import load_dotenv
# Create your views here.

def login(request):
    CLIENT_ID = os.environ.get('API_KEY')
    REDIRET_URL = os.environ.get('REDIRECT_URI')
    CLIENT_SECRET=os.environ.get('CLIENT_SECRET')
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}&client_secret={2}".format(
        CLIENT_ID, REDIRET_URL,CLIENT_SECRET)
    res = redirect(url)
    return res

def callback(request):
    code = request.GET['code']
    res = {
            'grant_type': 'authorization_code',
            'client_id': os.environ.get('API_KEY'),
            'redirect_url': os.environ.get('REDIRECT_URI'),
            'client_secret': os.environ.get('CLIENT_SECRET'),
            'code': code,
        }
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    response = requests.post("https://kauth.kakao.com/oauth/token", data=res, headers=headers)
    params='property_keys=["kakao_account.nickname"]'
    tokenJson = response.json()
    print(tokenJson)
    userUrl = "https://kapi.kakao.com/v2/user/me"
    auth = "Bearer "+tokenJson['access_token']
    HEADER = {
        "Authorization": auth,
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    res = requests.post(userUrl, headers=HEADER)
    print(res.json())
    user_json = res.json()
    kakao_account = res.json().get('kakao_account')
    if not kakao_account:
        return redirect('/predict')

    request.session['id'] = user_json['id']
    request.session['nickname']=user_json['kakao_account']['profile']['nickname']
    request.session['token'] = tokenJson['access_token']

    regionurl = 'http://'+os.environ.get('BACKEND_HOST')+":"+os.environ.get('BACKEND_PORT')+'/user/region'
    data={
        'id': request.session['id']
    }
    res = requests.get(regionurl,params=data) 
    reg_json=res.json()
    print ('로그인 정보:', request.session['id'], reg_json)
    if(reg_json['success'] and reg_json['data']['count'] > 0):
        return redirect('/')
    else:
        return redirect('/login/region')
    

def region(request):
    return render(request, 'home/region.html',{})

def submit(request):
    region = request.GET['region']
    reg2 = request.GET['reg2'] 

    url = 'http://'+os.environ.get('BACKEND_HOST')+":"+os.environ.get('BACKEND_PORT')+'/user/add'
    data={
        'id' : request.session['id'],
        'name': request.session['nickname'],
        'region': region,
        'reg2': reg2
    }
    res = requests.get(url, params=data)
    return redirect('/')

def logout(request):
    logoutUrl = "https://kapi.kakao.com/v1/user/logout"
    if 'token' in request.session:    
        HEADER = {
            "Authorization": request.session['token']
        }
        res = requests.get(logoutUrl, headers=HEADER)

        del request.session['token']
        del request.session['id']
        del request.session['nickname']
    return redirect('/')
