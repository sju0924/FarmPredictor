import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import date
import os

def get_param(prev_data):
    cur_year = date.today().year
    url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/InsttWeather/getWeatherYearMonList'
    params = {'serviceKey' : 'JmVxAGVsWxHDkatDGw5YlKfJn4iJKnsjTbD17s9mFVRH6n1U/FDHGHRxHQVT+KFXvxwkGoQAeixkTZoRWoFJAw==', 'Page_No' : '1', 'Page_Size' : '10', 'search_Year' : cur_year, 'obsr_Spot_Code' : '380959A001'}
    cur_data = api_reference(url, params)
    
    preded_data = cur_data.loc[:,['tmprt_150','arvlty_300','hd_150','soil_mitr_10','solrad_qy','date_time']]
    
    quat_info = pd.DataFrame(columns = preded_data.columns)
    quat_info['year_quat']=""    
    
    
    
    for quat in range(1,5):
        a = get_quater(preded_data, str(cur_year), quat)
        quat_info= quat_info.append(a, ignore_index = True)
    
    quat_info = quat_info.drop(['date_time'],axis=1)
    
    merged_data = []    
    
    d = quat_info[quat_info['year_quat'] == str(cur_year)+'_1']
    a = quat_info[quat_info['year_quat'] == str(cur_year)+'_2']
    b = quat_info[quat_info['year_quat'] == str(cur_year)+'_3']
    c = quat_info[quat_info['year_quat'] == str(cur_year)+'_4']

    d = d.drop(['year_quat'], axis = 1)
    a = a.drop(['year_quat'], axis = 1)
    b = b.drop(['year_quat'], axis = 1)
    c = c.drop(['year_quat'], axis = 1)

    idx = []
    for col in d.columns:
        col += '_1'
        idx.append(col)
    d.columns = idx        


    idx = []
    for col in a.columns:
        col += '_2'
        idx.append(col)
    a.columns = idx

    idx = []
    for col in b.columns:
        col += '_3'
        idx.append(col)
    b.columns = idx    

    idx = []
    for col in c.columns:
        col += '_4'
        idx.append(col)
    c.columns = idx


    d.reset_index(drop=True, inplace=True)
    a.reset_index(drop=True, inplace=True)
    b.reset_index(drop=True, inplace=True)
    c.reset_index(drop=True, inplace=True)

    e = pd.concat([d,a,b,c], axis = 1)

    merged_data.append(list(e.loc[0]))

    merged = pd.DataFrame(columns = e.columns)

    for data in merged_data:
        merged.loc[len(merged)] = data
    
   
    
    merged = merged.drop(['soil_mitr_10_2','soil_mitr_10_3','soil_mitr_10_4'], axis = 1)
    
    merged.columns= ['기온150CM_1', '풍향300CM_1', '습도150CM_1', '토양수분10CM_1', '일사량_1',
       '기온150CM_2', '풍향300CM_2', '습도150CM_2', '일사량_2', '기온150CM_3',
       '풍향300CM_3', '습도150CM_3', '일사량_3', '기온150CM_4', '풍향300CM_4',
        '습도150CM_4', '일사량_4']
    
    merged.loc[1] =(list(prev_data.loc[29][1:18]))
    
    
    
    merged = merged.fillna(method='ffill', limit=10)
    merged = merged.fillna(method='bfill', limit=10)
    
    return merged


#prev_data = pd.read_csv(os.getcwd()+'/data_analysis/mean_data.csv')
#a = get_param(prev_data)

a.iloc[0] # prediction parameter
