# Pandas - Panel Data 
import pandas as pd

# Series Object 
s1=pd.Series([2,3,1,4,6])
print(s1)

# Changing Index values like this 
s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s1) 

# Series Object from Dictionary 
# Dictionary is ordered , changeable and does not allow duplicates 
# Dictionary items are presented in key : value pairs, and can be referred to by using the key name. 
# Dictionaries are written with curly brackets 
d1=pd.Series({'a':1,'b':2,'c':3,'d':4})
print(d1)
# We can change the index values 
# d1=pd.Series({'a':1,'b':2,'c':3,'d':4},index=['d','b','c','a'])
d1=pd.Series(d1,index=['d','b','c','a'])
print(d1)

# Extracting Individual Elements
s1=pd.Series([1,2,3,4,5,6,7,8,9])
print(s1[3])  # Don't forget indexing starts with 0
print(s1[-3:]) #Extracting from back

# It will print first 4 elements
print(s1[:4] ) # Extracting sequence of elements  startinf with index 0 to 4 and since index 4 is exclusive so elements from 1 to 4 it will print

# Adding,Multiplying,Subtracting and Dividing Scalar value to Series Elements
print(s1+2)
print(s1-1)
print(s1*2)
print(s1/2)

# Arithematic Operations on Two Series Object 
s1=pd.Series([1,2,3])
s2=pd.Series([2,4,6])
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s2/s1)

# Dataframes

d1=pd.DataFrame({"Name" : ['Bob','Rose','Steve'],"Marks":[89,76,90]})
print(d1)
d2=pd.DataFrame({"Roll No":[1,2,3,4,5],"Name":['Rosy','Jennifer','Anne','Sophia','Emma'],"Total Marks Obatained":[90,78,98,85,89]})
print(d2)

# Basic Dataframe In-Built Functions 
# To read any csv file 

iris=pd.read_csv('iris_csv.csv') 
print(iris.head())
print(iris.head(10))
print(iris.tail())
print(iris.tail(10))
print(iris.shape)
print(iris.describe())
print(iris.iloc[4:10,0:2])
print(iris.loc[10:50,("sepalwidth","petalwidth")])
print(iris.drop("class",axis=1))    # Column Drop 
print(iris.drop([2,5,7],axis=0))    # Row drop
print(iris.mean())                  # Mean Function
print(iris.median())                # Median Function
print(iris.max())                   # Maximum Function
print(iris.min())                   # Minimum Function
