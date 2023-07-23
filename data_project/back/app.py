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
# 득점 분석 차트 정보 POST
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


# 실점 분석 차트 정보 POST
@app.route('/loss_chart')
def loss_chart():
    global df
    teamName = '맨시티'
    
    nameDf = df[df['홈'] == teamName]
    time = nameDf['시간']
    teamLoss = nameDf['실점']
    d = {
        'x': time.values.tolist(),
        'y': teamLoss.values.tolist(),
    }

    return json.dumps(d)

# 유효슈팅 당 득점 분석 막대그래프
@app.route('/shoot_chart')
def shoot_chart():
    global df
    teamName = '맨시티'

    nameDf = df[df['홈'] == teamName]
    teamShoot = nameDf['유효슈팅']
    teamScore = nameDf['득점']

    d = {
        'x': teamShoot.values.tolist(),
        'y': teamScore.values.tolist(),
    }

    return json.dumps(d)

# 점유율 당 득점 분석 산점도
@app.route('/share_chart')
def share_chart():
    global df 
    teamName = '맨시티'

    nameDf = df[df['홈'] == teamName]
    teamShare = nameDf['볼점유율']
    teamScore = nameDf['득점']

    d = {
        'x': teamShare.values.tolist(),
        'y': teamScore.values.tolist(),
    }

    return json.dumps(d)

# 홈팀과 원정팀의 시간 당 골 횟수 꺾은선 그래프
@app.route('/time_gain_chart')
def time_gain_chart():
    global df
    homeTeam = '맨시티'
    nameDf = df[df['홈'] == homeTeam]
    hteamScore = nameDf['득점']
    time = nameDf['시간']

    awayTeam = '리버풀'
    name = df[df['원정'] == awayTeam]
    ateamScore= name['득점']

    d = {
        'x': time.values.tolist(),
        'y1': hteamScore.values.tolist(),
        'y2': ateamScore.values.tolist(),
    }

    return json.dumps(d)

# 홈팀과 원정팀의 승리 횟수 비교 분석 막대그래프
@app.route('/win_count_chart')
def win_count_chart():
    homeTeam = '맨시티'
    home = df[df['홈'] == homeTeam]

    gain = home['득점'].values.tolist()
    loss = home['실점'].values.tolist()

    count = 0
    for i in range(len(gain)):
        if gain[i] > loss[i]:
            count += 1

        
    awayTeam = '리버풀'
    away = df[df['원정'] == awayTeam]

    gain = away['득점'].values.tolist()
    loss = away['실점'].values.tolist()

    count2 = 0
    for i in range(len(gain)):
        if gain[i] > loss[i]:
            count2 += 1

    d = {
        'x1': homeTeam.values.tolist(),
        'x2': awayTeam.values.tolist(),
        'y1': count.values.tolist(),
        'y2': count2.values.tolist(),
    }

    return json.dumps(d)


if __name__ == '__main__':
    app.run()
    

