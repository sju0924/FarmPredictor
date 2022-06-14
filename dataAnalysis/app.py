from flask import Flask, jsonify, request
from flask_restx import Resource, Api, reqparse
from flask_cors import CORS
import pickle
import joblib
import numpy as np
import pandas as pd
import os
from get_param import get_param
from get_prod import get_prod

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

@app.route('/data_analysis')
def data_main():
    return '<h1>Hello, Main</h1>'

@app.route('/data_analysis/predict')
def data_predict():
    crop = request.args.get('type', default = 'null', type = str)
    
    raw_data = pd.read_csv('mean_data.csv')
    print(raw_data)
    a = get_param(raw_data)
    
    
    temp_diff_1 = list(a.diff(axis=0).loc[0])[0]
    humidity_diff_1 = list(a.diff(axis=0).loc[0])[2]

    temp_diff_2 = list(a.diff(axis=0).loc[0])[5]
    humidity_diff_2 = list(a.diff(axis=0).loc[0])[7]
    data = a.loc[0]
    if crop == 'greenonion':
        model = joblib.load('tree_reg_pa.pkl')
    elif crop == 'chives':
        model = joblib.load('tree_reg_chok.pkl')
    elif crop == 'driedpepper':
        model = joblib.load('tree_reg_gun.pkl')
    elif crop == 'garlic':
        model = joblib.load('tree_reg_ma.pkl')
    elif crop == 'onion':
        model = joblib.load('tree_reg_yang.pkl')
    else:
        return{
            "success": 'False'
        }
    res = model.predict([data])
    res = float(res[0])
    result = get_prod(crop, res)
    return {
        "success": 'True',
        "type": crop,
        "result": result,
        "temp_diff_1": temp_diff_1,
        "temp_diff_2": temp_diff_2,
        "humidity_diff_1": humidity_diff_1,
        "humidity_diff_2":humidity_diff_2
    }

if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0")
    