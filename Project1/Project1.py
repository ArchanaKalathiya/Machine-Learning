# Advertisment Sale prediction from an existing customer 

import pandas
dataset=pandas.read_csv('dataset.csv') #Clasiification method  [Pandas - load CSV format dataset ]
dataset.shape   # no of rows and column
dataset.head(5) # Display first 5 row of dataset
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values #iloc(It helps us select a value that belongs to a particular row and column)
train_test_split(X,Y,test_size=0.25, random_state=0) #useful for validation , 25% of the data given to test 