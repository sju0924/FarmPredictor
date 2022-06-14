from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os
# Create your views here.
load_dotenv()
crop_rank = {'대파':0, '양파':0, '쪽파':0, '건고추':0, '마늘':0}
def predict_search(request):
    crops=[]
    rank = sorted(crop_rank.items(), key=lambda x: x[1], reverse=True)
    for i, item in enumerate(rank):
        crops.append({'name': item[0], 'rank':i+1 })
        
    return render(request, 'predict/search.html', {'crops': crops})

def predict_result(request):
    type = request.GET.get('type', None)
    
    if type == '대파':
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
        return {
            'msg': '검색 결과가 없습니다.',
            'success': False
        }
    
    data = requests.get('http://'+os.environ.get('host')+'/data_analysis/predict',{'type': code})
    jsondata = data.json()
    crop_rank[type] += 1;
    return render(request, 'predict/result.html',{
        'type': type, 
        'success': True,
        'res': jsondata['result'],
        "temp_diff_1": round(jsondata['temp_diff_1'],3),
        "temp_diff_2": round(jsondata['temp_diff_2'],3),
        "humidity_diff_1": round(jsondata['humidity_diff_1'],3),
        "humidity_diff_2":round(jsondata['humidity_diff_2'],3)})