# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:41:12 2022

@author: Asus
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

pima=pd.read_csv('F:/Online Class/4-1/zLabs/ML/diabetes_prediction_with_knn-master/diabetes.csv', encoding = 'utf8', engine = 'python')

# pd.options.display.max_rows = 10000
print(pima.to_string())

X = pima.iloc[:,0:8]
Y = pima.iloc[:,8]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

error = []

desired_k = 1000
min_err = 100000000.0

kvals = []

for i in range(1,250):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))
    err = np.mean(pred_i != y_test)
    if(min_err > err):
        min_err = err
        desired_k = i
    
    
    print(np.mean(pred_i != y_test))

# Plotting

plt.figure(figsize=(12,6))
plt.plot(range(1,250),error,color='red',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=10)
plt.title('Error Rate Vs. K value')
plt.xlabel('K value')
plt.ylabel('Mean error')    

print("Desired k-value is: ", desired_k)
print("Minimum error is: ", min_err)
