from flask import Flask
import numpy as np
from flask_cors import CORS
import json
import pandas as pd
import random

app = Flask(__name__)
CORS(app)

df = pd.read_csv("C:\\Users\\user\\Documents\\dev\\KKC_Python_Project\\data_project\\back\\data.csv", encoding='cp949')

@app.route('/')
def main():
    global df
    print(df['시간'])
    l = {
        'x' : df['시간'].values.tolist(),
        'y' : df['득점'].values.tolist()
    }
    res = json.dumps(l)
    return res

@app.route('/gain_chart')
def gain_chart():
    global df

    teamName = '맨시티'
    name = df[df['홈'] == teamName]
    teamScore = name['득점']
    time = name['시간']
    l = {
        'x' : time.values.tolist(),
        'y' : teamScore.values.tolist(),
    }
    res = json.dumps(l)
    return res

if __name__ == '__main__':
    app.run()
    

