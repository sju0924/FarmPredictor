import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def article_parsing(url):
    # request error를 피하기 위한 header 설정
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    # html parser
    web = BeautifulSoup(requests.get(url, allow_redirects=False, headers=header).text, 'html.parser')

    # 제목
    title = web.find("meta", property="og:title")['content']

    # 요약 내용
    description = web.find('meta', property="og:description")['content']
    
    # 대표 이미지 url
    image_url = web.find("meta", property="og:image")['content']

    # 대표이미지 객체
    image = Image.open(BytesIO(requests.get(image_url, headers=header).content))
    
    return {'title':title, 'description' : description, 'image': image, 'image_url':image_url, 'url':url }

print(article_parsing('https://n.news.naver.com/article/092/0002260682?cds=news_media_pc&type=editn'))