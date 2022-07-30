
#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### data preprocessing ###


#import dataset
dataset = pd.read_csv('score.csv')

#select independent variables
X = dataset.drop(columns = ['Scores'], axis = 1)
Y = dataset.drop(columns = ['Hours'], axis = 1)

#Split dataset into Training and Test Cases
from sklearn.model_selection import train_test_split
X_train,X_test, Y_train,Y_test = train_test_split(X , Y , test_size = 0.25)

#Fitting Simple Regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train , Y_train)

y_pred = regressor.predict(X_test)

#plot 
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.show()

#model Evaluation
import sklearn.metrics
acc = regressor.score(X_test, Y_test)
print("Accuracy: ", round(100*acc,2))
print("Mean Absolute Error: ",round(sklearn.metrics.mean_absolute_error(Y_test,y_pred),2))
print("Mean Squared Error: ", round(sklearn.metrics.mean_squared_error(Y_test,y_pred),2))

#prediction
print("Marks of student who studied 9.2 hours a day:  ", regressor.predict([[9.2]]))
