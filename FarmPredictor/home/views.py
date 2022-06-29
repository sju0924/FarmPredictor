from django.shortcuts import render
import os
import sys
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from dotenv import load_dotenv
# Create your views here.
def search_news(word):    
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    url = "https://openapi.naver.com/v1/search/news.json?query="+word+"&display="+"3" # json 결과
    header={
        'X-Naver-Client-Id': os.environ.get('NAVER_CLIENT'),
        'X-Naver-Client-Secret':os.environ.get('NAVER_SECRET'),
    }
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    res = requests.get(url,headers=header)
    res_json = res.json()
    return res_json
    
def article_parsing(url):
    # request error를 피하기 위한 header 설정
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    # html parser
    web = BeautifulSoup(requests.get(url, allow_redirects=False, headers=header).text, 'html.parser')
    
    try:
        title = web.find("meta", property="og:title")['content']

        # 요약 내용
        description = web.find('meta', property="og:description")['content']
        
        # 대표 이미지 url
        image_url = web.find("meta", property="og:image")['content']
        print(title, description, image_url)
        # 대표이미지 객체
        
        return {'title':title, 'description' : description,  'image_url':image_url, 'url':url, 'success':True }
    except :
        return{'success':False}

def index(request):
    if 'nickname' in request.session:
        nick = request.session['nickname']   
    else:
        nick = ""
    words=search_news('감자 가격')
    news=[]
    for item in words['items']:
        data = article_parsing(item['link'])
        if data['success']:
            news.append(data)
        
    
    print(news)
    return render(request, 'home/index.html',{'page':{'title':'홈'}, 'nickname':nick,'news':news})