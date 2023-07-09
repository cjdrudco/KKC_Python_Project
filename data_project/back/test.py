import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("C:\\Users\\user\\Documents\\dev\\KKC_Python_Project\\data_project\\back\\data.csv", encoding='cp949')
x = df['시간']
y = df['득점']
plt.plot(x, y)
plt.show()
