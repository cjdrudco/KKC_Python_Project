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
# 홈팀 득점 분석 차트 정보 POST
@app.route('/home_gain_chart')
def home_gain_chart():
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


# 원정팀 득점 분석 차트 정보 POST
@app.route('/away_gain_chart')
def away_gain_chart():
    global df

    teamName = '맨시티'
    name = df[df['원정'] == teamName]
    teamScore = name['득점']
    time = name['시간']
    l = {
        'x' : time.values.tolist(),
        'y' : teamScore.values.tolist(),
    }
    res = json.dumps(l)
    return res


# 홈팀 실점 분석 차트 정보 POST
@app.route('/home_loss_chart')
def home_loss_chart():
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

# 원정팀 실점 분석 차트 정보 POST
@app.route('/away_loss_chart')
def away_loss_chart():
    global df
    teamName = '맨시티'
    
    nameDf = df[df['원정'] == teamName]
    time = nameDf['시간']
    teamLoss = nameDf['실점']
    d = {
        'x': time.values.tolist(),
        'y': teamLoss.values.tolist(),
    }

    return json.dumps(d)

# 홈팀 유효슈팅 당 득점 분석 막대그래프
@app.route('/shoot_chart')
def home_shoot_chart():
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

# 원정팀 유효슈팅 당 득점 분석 막대그래프
@app.route('/away_shoot_chart')
def away_shoot_chart():
    global df
    teamName = '맨시티'

    nameDf = df[df['원정'] == teamName]
    teamShoot = nameDf['유효슈팅']
    teamScore = nameDf['득점']

    d = {
        'x': teamShoot.values.tolist(),
        'y': teamScore.values.tolist(),
    }

    return json.dumps(d)


#홈팀의 최근 3경기 전적 표
@app.route('/home_game_chart')
def home_game_chart():
    global df
    teamName = '맨시티'

    topThreeDf = df[df['홈'] == teamName].head(3)

    d = {
        '시간' : topThreeDf['시간'].values.tolist(),
        '득점' : topThreeDf['득점'].values.tolist(),
        '실점' : topThreeDf['실점'].values.tolist(),
        '원정' : topThreeDf['원정'].values.tolist(),

    }

    return json.dumps(d, ensure_ascii=False)

#원정팀의 최근 3경기 전적 표
@app.route('/away_game_chart')
def away_game_chart():
    global df
    teamName = '맨시티'

    topThreeDf = df[df['원정'] == teamName].head(3)

    d = {
        '시간' : topThreeDf['시간'].values.tolist(),
        '득점' : topThreeDf['득점'].values.tolist(),
        '실점' : topThreeDf['실점'].values.tolist(),
        '홈' : topThreeDf['홈'].values.tolist(),


    }

    return json.dumps(d, ensure_ascii=False)

# 홈팀 점유율 당 득점 분석 산점도
@app.route('/home_share_chart')
def home_share_chart():
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

# 원정팀 점유율 당 득점 분석 산점도
@app.route('/away_share_chart')
def away_share_chart():
    global df 
    teamName = '맨시티'

    nameDf = df[df['원정'] == teamName]
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

#홈팀과 원정팀의 상대전적 표
@app.route('/home_record_chart')
def home_record_chart() :
    global df
    homeTeam = '맨시티'
    awayTeam = '리버풀'

    temp = df[df['홈'] == homeTeam]
    temp = temp[temp['원정'] == awayTeam]

    d = {
        '시간': temp['시간'].values.tolist(),
        '홈': temp['홈'].values.tolist(),
        '원정': temp['원정'].values.tolist(),
        '득점': temp['득점'].values.tolist(),
        '점유율': temp['볼점유율'].values.tolist(),

    }

    return json.dumps(d, ensure_ascii=False)

#원정팀과 홈팀의 상대전적 표
@app.route('/away_record_chart')
def away_record_chart() :
    global df
    homeTeam = '리버풀'
    awayTeam = '맨시티'

    temp = df[df['홈'] == homeTeam]
    temp = temp[temp['원정'] == awayTeam]

    d = {
        '시간': temp['시간'].values.tolist(),
        '홈': temp['홈'].values.tolist(),
        '원정': temp['원정'].values.tolist(),
        '득점': temp['득점'].values.tolist(),
        '점유율': temp['볼점유율'].values.tolist(),

    }

    return json.dumps(d, ensure_ascii=False)

# 홈팀과 원정팀의 승리 횟수 비교 분석 막대그래프
@app.route('/win_count_chart')
def win_count_chart():
    global df
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
        'x1': homeTeam,
        'x2': awayTeam,
        'y1': count,
        'y2': count2,
    }
    return json.dumps(d, ensure_ascii=False)

# 홈팀의 점유율 평균
@app.route('/home_avg_chart')
def home_avg_chart():
    global df
    teamName = '리버풀'
    team = df[df['홈'] == teamName]

    k = team['볼점유율'].values.tolist()
    t = []
    for item in k:
        t.append(int(item.replace('%', '')))

    avg = sum(t) / len(t)


    d = {
        'x': avg,
    }

    return json.dumps(d)

#원정팀의 점유율 평균
@app.route('/away_avg_chart')
def away_avg_chart():
    global df
    teamName = '리버풀'
    team = df[df['원정'] == teamName]

    k = team['볼점유율'].values.tolist()
    t = []
    for item in k:
        t.append(int(item.replace('%', '')))

    avg = sum(t) / len(t)


    d = {
        'x': avg,
    }

    return json.dumps(d)






if __name__ == '__main__':
    app.run()
    

