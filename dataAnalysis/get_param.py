import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import date
import os

def api_reference(url, params):
    contents = requests.get(url, params=params)
    soup = BeautifulSoup(contents.text)
    rows = soup.find_all("item")
    row_list = [] # 행값
    name_list = [] # 열이름값
    value_list = [] #데이터값

    # xml 안의 데이터 수집
    for i in range(0, len(rows)):
        columns = rows[i].find_all()
        #첫째 행 데이터 수집
        for j in range(0,len(columns)):
            if i ==0:
                # 컬럼 이름 값 저장
                name_list.append(columns[j].name)
            # 컬럼의 각 데이터 값 저장
            value_list.append(columns[j].text)
        # 각 행의 value값 전체 저장
        row_list.append(value_list)
        # 데이터 리스트 값 초기화
        value_list=[]
        
    

    df = pd.DataFrame(row_list, columns=name_list)
    #df = df.drop(['fmapinnb','pnulnmcd','fmapbdcrd','gml:multipolygon','gml:polygonmember','gml:polygon','gml:outerboundaryis','gml:linearring','gml:coordinates','intprcd'], axis = 1)
    #df = df.replace("0.0", np.NaN)
    #df = df.replace("0", np.NaN)
    #df = df.replace("", np.NaN)
    #df = df.replace("X", np.NaN)
    #df = df.replace("-", np.NaN)
    #df = df.dropna(axis = 1)
    
    return df


def get_quater(raw_data, year, quat):
    
    if(quat == 1):
        month = [year+'-01',year+'-02',year+'-03']    
    elif(quat == 2):
        month = [year+'-04',year+'-05',year+'-06']
    elif(quat == 3):
        month = [year+'-07',year+'-08',year+'-09']
    elif(quat == 4):
        month = [year+'-10',year+'-11', year+'-12']
    
    
    months = '|'.join(month)
    df = raw_data[raw_data['date_time'].str.contains(months)]
    
    
    df = df.drop(['date_time'], axis = 1)

    df = df.astype(float)
    df = df.fillna(method='ffill', limit=10)
    df = df.fillna(method='bfill', limit=10)
    df = df.fillna(df.mean())
    y_quat = year+'_'+str(quat)
    result = dict(df.mean())
    result['year_quat'] = y_quat
    return result


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
    
    merged.loc[1] =(list(prev_data.loc[30][1:18]))
    
    
    
    merged = merged.fillna(method='ffill', limit=10)
    merged = merged.fillna(method='bfill', limit=10)
    
    
    merged = merged.reindex(index=[1,0])
    
    return merged


#prev_data = pd.read_csv(os.getcwd()+'/data_analysis/mean_data.csv')
#a = get_param(prev_data)

#a.diff(axis=0).loc[0]
