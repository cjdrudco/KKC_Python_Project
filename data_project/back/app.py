from flask import Flask
import numpy as np
from flask_cors import CORS
import json
import pandas as pd
import random

app = Flask(__name__)
CORS(app)

df = pd.read_csv("C:/Users/User/Documents/dev/김경찬/data/data_project/back/data.csv", encoding='cp949')

@app.route('/')
def main():
    labels = ["January", "February", "March", "April", "May", "June"]
    l = {
        'labels': labels,
        'datasets': [
            {
                'label': "My First dataset",
                'backgroundColor': "rgb(255, 99, 132)",
                'borderColor': "rgb(255, 99, 132)",
                'data': [50, 5, 2, 7, 30, 20, 45],
            },
        ],
    }
    res = json.dumps(l)
    return res

@app.route('/category_tolist')
def category_tolist():
    global df
    category = '홈'
    home_list = pd.DataFrame(df[category]).values.tolist()
    l = []
    
    for t in home_list:
        l.append(t[0])
        
    d = {
        'test': l
    }
    
    res = json.dumps(d, ensure_ascii=False)
    return res

@app.route('/home_time_socre_tochart')
def home_time_socre():
    global df
    teamList = ['첼시', '리버풀', "맨시티"]
    
    frameList = []
    for teamName in teamList:
        temp = df[df['홈'] == teamName]
        temp.sort_values(by='시간')
        frameList.append(temp)

    time = []
    temp = pd.DataFrame(frameList[0]['시간']).values.tolist()
    for t in temp:
        time.append(t[0][:10]) 
    
    scores = []
    for frame in frameList:
        score = []
        temp = pd.DataFrame(frame['득점']).values.tolist()
        for t in temp:
            score.append(t[0])
        scores.append(score)
    
    
    datasets = []
    for i in range(len(teamList)):
        color = "rgb(" + str(random.randrange(0,255)) + "," + str(random.randrange(0,255)) + "," + str(random.randrange(0,255)) + ")"
        datasets.append({
            'label': teamList[i],
            'backgroundColor': color,
            'borderColor': color,
            'data': scores[i]
        })
    
    res = json.dumps({
        'labels': time,
        'datasets': datasets,
    }, ensure_ascii=False)
    
    return res

if __name__ == '__main__':
    app.run()
    

