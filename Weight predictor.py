# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cf_B8Moeyj4fcJoQUaYTkXuKDThHxKjz
"""

#from google.colab import files
#a=files.upload()

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("weight.csv")
data.head()

x=data.iloc[:,0].values
y=data.iloc[:,1].values

x=x.reshape(-1,1)
y=y.reshape(-1,1)

#checking null data
data.isnull().sum()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

reg=RandomForestRegressor(n_estimators=1000,random_state=0)
reg.fit(x_train,y_train)

pred_y=reg.predict(x_test)

#calculating both r_square and min_square error
print('R square error=',metrics.r2_score(y_test,pred_y))
print('min square error=',metrics.mean_squared_error(y_test,pred_y))

x_grid=np.arange(min(x_train),max(x_train),0.01)
x_grid=x_grid.reshape(len(x_grid),1)
plt.scatter(x_train,y_train,color='blue')
plt.plot(x_grid,reg.predict(x_grid),color='red')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight plot")
plt.show()
