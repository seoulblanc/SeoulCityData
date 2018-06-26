from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

import numpy
import pandas as pd
import tensorflow as tf

seed = 0

numpy.random.seed(seed)
tf.set_random_seed(seed)

df = pd.read_csv('c:/pythondata/201803_coffee_8category02.csv', delimiter=',')

print(len(df))

dataset = df.values

X = dataset[:, 1:9]
Y = dataset[:, 9]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=seed)

model = Sequential()
model.add(Dense(24, input_dim =8, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, Y_train, epochs=500, batch_size=10)
Y_prediction = model.predict(X_test).flatten()

for i in range(10):
    lable = Y_test[i]
    prediction = Y_prediction[i]
    print('실제매출: {: .3f}, 예상매출: {: .3f}'. format(lable, prediction))

# 내가 원하는 값 추가로 넣어 보기

test = numpy.array([[439101270,359260519,89809978,30785703,270403472,192142283,32227606,1195082177]])
result = float(229803235)

Y_prediction1 = model.predict(test).flatten()
print('실제매출: {: .3f}' .format(229803235))

predic = str(Y_prediction1).strip('[]')
predic = float(predic)
print('예상매출: {: .3f}' .format(predic))


