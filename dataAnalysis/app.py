from flask import Flask, jsonify, request
from flask_restx import Resource, Api, reqparse
from flask_cors import CORS
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
model = pickle.load(open('tree_reg.pkl','rb'))

@app.route('/data_analysis')
def data_main():
    return '<h1>Hello, Main</h1>'

@app.route('/data_analysis/predict')
def data_predict():
    crop = request.args.get('type', default = 'null', type = str)
    return {
        "type": crop
    }

if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0")