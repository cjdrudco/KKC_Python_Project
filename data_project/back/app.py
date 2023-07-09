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
    l = {
        'x' : df['시간'],
        'y' : df['득점']
    }
    res = json.dumps(l)
    return res

def prediction():
    pass

if __name__ == '__main__':
    app.run()
    

