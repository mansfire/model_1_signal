# -*- coding: utf-8 -*-
"""examplemodel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KFC7tES1289U2XrBlUggr1fODGHNukI8
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from matplotlib import pyplot
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import explained_variance_score, mean_squared_error, r2_score, mean_absolute_error
from collections import Counter
from keras import callbacks
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout,InputLayer
from tensorflow.keras.models import Sequential
from keras.layers import BatchNormalization
from tensorflow.keras import regularizers
from tensorflow.keras import backend
from random import shuffle
from keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import RMSprop
import warnings
warnings.filterwarnings("ignore")

from google.colab import drive

data=pd.read_csv('/content/InputData.csv')
data.head(2)

#initialize and gather data

data = pd.read_csv('/content/InputData.csv')

data.astype(np.float32)

data=data.drop(['idx'],axis=1)
  #split the data
    #again, ke is exit as we want to see how we can prevent this from occuring
  ##Splitting Independent and dependent variable in X and Y respectively
X = data.drop(['signal_after'],axis=1)
Y = data[['signal_after']].values

print(X.shape)
print(Y.shape)
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.1)
X_train = X_train.astype(np.float64)

y_train = y_train.astype(np.float64)


  # build the model!
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
model = Sequential()
model.add(Dense(1000, input_shape=(X_train.shape[1],), activation='relu')) # (features,)
model.add(Dropout(0.2))
model.add(Dense(750, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(500, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(250, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(150, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(75, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(1, activation='linear')) # output node
model.summary() # see what your model looks like

  # compile the model
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

  # early stopping callback
es = EarlyStopping(monitor='val_loss',
                  mode='min',
                  patience=1000,
                  restore_best_weights = True)

  # fit the model!q
  # attach it to a new variable called 'history' in case
  # to look at the learning curves
cp_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath="/content",
    verbose=1,
    save_weights_only=True,
    save_freq=100)


history = model.fit(X_train, y_train,
                    validation_data = (X_test, y_test),

                    epochs=50000,
                    callbacks=es,
                    batch_size=32,
                    verbose=1)
pred = model.predict(X_test)
pred

trainpreds = model.predict(X_train)

from sklearn.metrics import mean_absolute_error
pred_mae=mean_absolute_error(y_train, trainpreds)


print(mean_absolute_error(y_train, trainpreds)) # train
print(mean_absolute_error(y_test, pred)) # test
out_preds=(pred,trainpreds)

  #Read in the data from excel (I converted form csv)

X

!pip install h5py

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
pred = model.predict(X_test)
pred

trainpreds = model.predict(X_train)

from sklearn.metrics import mean_absolute_error
pred_mae=mean_absolute_error(y_train, trainpreds)


print(mean_absolute_error(y_train, trainpreds)) # train
print(mean_absolute_error(y_test, pred)) # test
out_preds=(pred,trainpreds)

Predictors=['router_x',	'router_y',	'cell_x',	'cell_y',
            'pass_0',	'pass_dis_0',	'pass_type_0',	'pass_mat_0',
            'pass_1',	'pass_dis_1',	'pass_type_1',	'pass_mat_1',
            'pass_2',	'pass_dis_2',	'pass_type_2',	'pass_mat_2',
            'pass_3',	'pass_dis_3',	'pass_type_3',	'pass_mat_3',
            'pass_4',	'pass_dis_4',	'pass_type_4',	'pass_mat_4',
            'pass_5',	'pass_dis_5',	'pass_type_5',	'pass_mat_5',
            'pass_6',	'pass_dis_6',	'pass_type_6',	'pass_mat_6',
            'pass_7',	'pass_dis_7',	'pass_type_7',	'pass_mat_7',
            'pass_8',	'pass_dis_8',	'pass_type_8',	'pass_mat_8',
            'signal_start']
TestingData=pd.DataFrame(data=X_test, columns=Predictors)
TestingData['Loss']=y_test[:,0]
TestingData['Predicted_Loss']=pred[:,0]
TestingData['Error_Loss']=abs(y_test[:,0]-pred[:,0])/(y_test[:,0])*100

TestingData.head(10)

np.savetxt("/conent/o.csv",TestingData,delimiter=",")

pred

data2.head()

data2.head()



data2

d2

a=np.setdiff1d(data2.columns,X_train.columns)

a

pred = model.predict(data2)
pred

Predictors=['router_x',	'router_y',	'router_z',	'cell_x',	'cell_y',	'cell_z',	'Distance',	'orientation_x',	'orientation_y',	'orientation_z',
            'pass_0',	'pass_dis_0',	'pass_type_0',	'pass_mat_0',
            'pass_1',	'pass_dis_1',	'pass_type_1',	'pass_mat_1',
            'pass_2',	'pass_dis_2',	'pass_type_2',	'pass_mat_2',
            'pass_3',	'pass_dis_3',	'pass_type_3',	'pass_mat_3',
            'pass_4',	'pass_dis_4',	'pass_type_4',	'pass_mat_4',
            'pass_5',	'pass_dis_5',	'pass_type_5',	'pass_mat_5',
            'pass_6',	'pass_dis_6',	'pass_type_6',	'pass_mat_6',
            'pass_7',	'pass_dis_7',	'pass_type_7',	'pass_mat_7',
            'pass_8',	'pass_dis_8',	'pass_type_8',	'pass_mat_8',
            'signal_start']
TestingData=pd.DataFrame(data=data2, columns=Predictors)
TestingData['Predicted_Loss']=pred
TestingData.head()

fig=plt.figure(figsize=(10,7))
ax=plt.axes(projection="3d")
ax.scatter(data2['router_x'],data2['router_y'],data2['router_z'])
data2['router_x']

data2['router_x']

x_test

