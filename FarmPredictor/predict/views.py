from django.shortcuts import render
import requests
# Create your views here.
def predict_search(request):
    
    
    crops=[
        {'name': '감자', 'rank':1},
        {'name': '양파', 'rank':2},
        {'name' : '대파', 'rank':3}
        
    ]
    return render(request, 'predict/search.html', {'crops': crops})

def predict_result(request):
    type = request.GET.get('type', None)
    
    if type == '양퍄':
        code = 'greenonion'
    elif type== '쪽파':
        code = 'chives'
    elif type == '건고추':
        code = 'driedpepper'
    elif type == '마늘':
        code = 'garlic'
    elif type == '양파':
        code ='onion'
    else:
        return '검색 결과가 없습니다.'
    
    data = requests.get('http://127.0.0.1/data_analysis/predict',{'type': code})
    
    return render(request, 'predict/result.html',{'type': type, 'res': data.result})