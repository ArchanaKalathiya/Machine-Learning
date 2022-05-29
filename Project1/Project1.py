# Advertisment Sale prediction from an existing customer 

import pandas as pd #useful for loading dataset
import numpy as np  #to perform array

#Load data and print it 
dataset = pd.read_excel('dataset.xlsx') #Clasiification method  [Pandas - load CSV format dataset ]
print(dataset)
print(dataset.shape)   # no of rows and column
print(dataset.head(5)) # Display first 5 row of dataset
print(dataset.tail(5)) #It will print last 5 lines

#segregation of dataset 
X = dataset.iloc[:,:-1].values
X #prints input values 
Y = dataset.iloc[:,-1].values #iloc(It helps us select a value that belongs to a particular row and column)
Y #print output values 

#Train and test 
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25, random_state=0) #useful for validation , 25% of the data given to test 

#Feature Scaling 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
print(X_train)


# model.fit(X_train,Y_train)
# result = model.predict(sc.transform(newCust)

#Training using logistic algorithm
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)
