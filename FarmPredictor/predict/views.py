from django.shortcuts import render
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
    return render(request, 'predict/result.html',{'type': type})