# Sigmoid 와 Lelu 함수를 활용한 이항분류 예시 코드
# 히든 레이어 2개의 층 생성 
# 15개의 input 요소에 대하여 학습

from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import tensorflow as tf
import pandas as pd

df = pd.read_csv('c:/pythondata/seouldata0621_2.csv', delimiter=',',
                 names = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])
print(df.head(5))
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15,15))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
plt.show()

dataset = df.values

X = dataset[:, 0:15].astype(float)
Y = dataset[:, 16]

model = Sequential()
model.add(Dense(15, input_dim=15, activation='relu'))
model.add(Dense(15, activation='sigmoid'))
model.add(Dense(1, activation='relu'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X,Y, epochs=200, batch_size=10)
print('\n accuracy : %.4f' %(model.evaluate(X,Y)[1]))


