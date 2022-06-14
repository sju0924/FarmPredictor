
# 호출 예시 get_prod('마늘', 7000)
# pred는 예측 된 생산량
import pandas as pd

def get_prod(crop_name, pred):
    production = pd.read_csv(crop_name + '_생산량.csv', encoding = 'cp949')
    production = production.drop(0)
    production = production.drop(1)
    prod_list = list(production.loc[:,['2017','2018','2019','2020']].loc[12])
    prod_list = list(map(float,prod_list))
    prod_list.append(pred)
    
    stand = sum(prod_list)/len(prod_list)
    
    rel_pred = (pred*100/stand)
    
    
    if(rel_pred<=95):
        return "흉작"
    elif(rel_pred>=110):
        return "생산량 증가"
    else:
        return "평년수준 생산량"
