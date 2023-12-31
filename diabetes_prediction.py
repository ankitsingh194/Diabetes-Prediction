# -*- coding: utf-8 -*-
"""Diabetes Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l2ibocnfhu2h_2x4oswgXfNa__aZMhq9
"""

import pandas as pd
import numpy as np
from  sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

diabetes_data = pd.read_csv('/content/diabetes.csv')

diabetes_data.head()

diabetes_data.describe()

diabetes_data.shape

"""0 --> Non-Diabetic
1 --> Diabetic
"""

diabetes_data['Outcome'].value_counts()

diabetes_data.groupby('Outcome').mean()

X = diabetes_data.drop(columns='Outcome', axis=1)
Y = diabetes_data['Outcome']

print(Y)

print(X)

"""Data standerdization"""

scaler= StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_data['Outcome']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y , random_state=2)

print(X_train.shape,X_test.shape)

print(Y_train.shape,Y_test.shape)

classifier = svm.SVC(kernel='linear')

classifier.fit(X_train,Y_train)

"""model Evaluation


accuracy score
"""

X_train_pre = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_pre, Y_train)

print(training_data_accuracy)

X_test_pre = classifier.predict(X_test)
training_data_accuracy = accuracy_score(X_test_pre, Y_test)

print(training_data_accuracy)

"""Making a Predictive System"""

input_data = (7,106,92,18,0,22.7,0.235,48)

# change this into numpyarray

input_data_as_numpyarray = np.asarray(input_data)

#reshape the array

input_data_reshaped = input_data_as_numpyarray.reshape(1,-1)

#standardize the input data


standardized_input_data = scaler.transform(input_data_reshaped)

prediction = classifier.predict(standardized_input_data)
print(prediction)

if prediction[0] == 0:
  print('the preson is not diabetic' )
else :
  print('the preson is  diabetic' )