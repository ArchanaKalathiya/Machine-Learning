# Matplotlib 

import numpy as np
from matplotlib import pyplot as plt

# Line Plot 
x=np.arange(1,11)
print(x)
y=2*x
print(y)
plt.title("Line PLot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x,y,color="m",linestyle=':',linewidth=2)
plt.show()

# Adding 2 lines in the same plot
x=np.arange(1,11)
y1=2*x
y2=3*x
plt.plot(x,y1,color="red",linestyle="--",linewidth=3)
plt.plot(x,y2,color="blue",linestyle="dashdot",linewidth=3)
plt.title("Two Lines Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# SubPlots
x=np.arange(1,11)
y1=2*x
y2=3*x
plt.subplot(1,2,1)
plt.plot(x,y1,color="red",linestyle="--",linewidth=3)
plt.title("Two Lines Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(x,y2,color="blue",linestyle="dashdot",linewidth=3)
plt.title("Two Lines Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# Bar Plot - It helps to understand the categorical column
student={"Bob":87,"Matt":56,"Sam":77}    # Dictionary Student
# Both axis have numerical entity
names=list(student.keys())      # names is converted into a list which is object called as keys
values=list(student.values())
plt.bar(names,values)
plt.show()

# Bar Plot 2

Subjects={"Math":97,"Science":87,"English":89,"Histroy":90}
sub=list(Subjects.keys())
marks=list(Subjects.values())
plt.bar(sub,marks)
plt.title("Marks Scored by Bob in these subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks Obtained")
plt.grid(True)
plt.show()

# Horizontal Bar Plot ( Use barh instead of bar)
Subjects={"Math":97,"Science":87,"English":89,"Histroy":90}
sub=list(Subjects.keys())
marks=list(Subjects.values())
plt.barh(sub,marks,color='m')
plt.title("Marks Scored by Bob in these subjects")
plt.xlabel("Marks Obtained")
plt.ylabel("Subjects")
plt.grid(True)
plt.show()

# Scatter Plot - TO understand distribution between two numerical entities . These entities represented in the form of Datapoints
x=[10,20,30,40,50]
y=[5,4,3,2,1]
plt.scatter(x,y,marker="*",color='purple',s=10)  #To change the shape of plot use marker 
#plt.sctter(x,y,marker="*",c="g",s=100)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Adding two markers in the same plot
x=[10,20,30,40,50]
a=[1,2,3,4,5]
b=[5,4,3,2,1]
plt.scatter(x,a,marker="*",color='purple',s=30)
plt.scatter(x,b,marker="d",color='y',s=30)
plt.title("Adding two markers in same plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


#Bar plot in Subplots

x=[10,20,30,40,50]
y=[5,4,3,2,1]
plt.subplot(2,1,1)
plt.scatter(x,y,marker="v",color='purple',s=50)  #To change the shape of plot use marker 
#plt.sctter(x,y,marker="*",c="g",s=100)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

x=[10,20,30,40,50]
a=[1,2,3,4,5]
b=[5,4,3,2,1]
plt.subplot(2,1,2)
plt.scatter(x,a,marker="h",color='purple',s=30)
plt.scatter(x,b,marker="d",color='y',s=30)
plt.title("Adding two markers in same plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Histogram - Ditribution of Continuous numerical data 
# it creates peak (peak shows how many times the number occurs in the data variable ) 
data=[1,2,3,3,4,2,5,2,6,4,7,8,4,8,9]
plt.hist(data,color='g',bins=4)   # bins are the number of bars
plt.show()


# Histogram using a dataset
import pandas as pd
iris=pd.read_csv('iris_csv.csv')
print(iris.head())
plt.hist(iris['sepallength'],bins=50)
plt.show()

# Box Plot - It basically gives the 5 number summary
one =[1,2,3,4,5,6,7,8,9]
two =[1,2,3,4,5,4,3,2,1]
three=[6,5,7,2,5,1,3,5,2] 
data = list([one,two,three])
plt.boxplot(data)
plt.show()

# Upper part of the boxplot says the maximum value
# Box containing a middle colored line will be meidan 
# Lower part of the boxplot says the minimum value

# Boxplot 2
l1=[1,2,4,2,5,7,2,5,8]
l2=[2,3,1,4,5,8,6,3,1]
l3=[9,5,2,5,3,7,2,1,8]
data = list([l1,l2,l3])
plt.boxplot(data)
plt.show()

# Violin-Plot
one =[1,2,3,4,5,6,7,8,9]
two =[1,2,3,4,5,4,3,2,1]
three=[6,5,7,2,5,1,3,5,2] 
data = list([one,two,three])
plt.violinplot(data,showmedians=True) # Showmedians show the lines or indicators( Means the median lines)
plt.show()

# Violin-plot 2
l1=[1,2,4,2,5,7,2,5,8]
l2=[2,3,1,4,5,8,6,3,1]
l3=[9,5,2,5,3,7,2,1,8]
data = list([l1,l2,l3])
plt.violinplot(data,showmedians=True)
plt.show()

# Pie-chart 
fruit=['Mango','Pineapple','Muskmelon','Watermelon','Dragon-fruit']
quantity=[89,87,54,70,80]
plt.pie(quantity,labels=fruit) #in pie first pass numerical entity and then categorical entity
plt.show()

# Change the colors of different sectors in pie-chart (to add percentage we use autopct)
# autopct='%0.1f%%'colors=[
# "y","r","m","g"]
fruit=['Mango','Tomato','Muskmelon','Watermelon','Dragon-fruit']
quantity=[89,87,54,70,80]
plt.pie(quantity,labels=fruit,autopct='%0.1f%%',colors=['gold','tomato','bisque','g','deeppink']) #in pie first pass numerical entity and then categorical entity
plt.show()

# DounghNut-Chart
fruit=['Mango','Tomato','Muskmelon','Watermelon','Dragon-fruit']
quantity=[89,87,54,70,80]
plt.pie(quantity,labels=fruit,autopct="%0.1f%%",colors=['gold','tomato','bisque','g','deeppink'],radius=1) 
plt.pie([5],colors=['w'],radius=0.5)
plt.show()

#Dough_Nut-Chart 2
fruit=['Apple','Orange','Mango','Guava']
quantity=[67,34,100,29]
plt.pie(quantity,labels=fruit,radius=1)
plt.pie([1],colors=['w'],radius=0.5)
plt.show()