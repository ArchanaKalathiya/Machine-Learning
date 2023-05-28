# NumPy Library
import numpy as np

# Intializing arrays
# One dimensional Array
n1 = np.array([10, 20, 30, 40])
# Multi-dimensional Array
n2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(n1)
print(n2)

# Intialize Arrays with zeros
n1 = np.zeros((1, 2))
n2 = np.zeros((3, 5))
print(n1)
print(n2)

# Initialize Arrays with same numbers
n1 = np.full((4, 8), 3)
n2 = np.full((1, 1), 2)
print(n1)
print(n2)

# Intialize Arrays within a range
n = np.arange(2, 10)
print(n)
y=np.arange(1,14,3)
print(y)

#Intialize Arrays with random numbers
x=np.random.randint(1,100)
print(x)
x=np.random.randint(1,100,10) # 10 indicates  we want 10 random numbers in this given range  
print(x)

# NumPy Shape
print(n1.shape)
print(y.shape)
print(x.shape)

# Stacking Methods 
n1=np.array([10,20,30])
n2=np.array([40,50,60])
# Vertical Stacking Method 
print(np.vstack((n1,n2)))
print(np.vstack((n2,n1)))
#Horizontal Stacking Method
print(np.hstack((n1,n2)))
print(np.hstack((n2,n1)))
#Column wise stacking Method
print(np.column_stack((n1,n2)))
print(np.column_stack((n2,n1)))

# Numpy Intersection and Difference 
n1=np.array([10,20,30,40,50])
n2=np.array([40,50,60,70])
print(np.intersect1d(n1,n2))
print(np.intersect1d(n2,n1))
print(np.setdiff1d(n1,n2))
print(np.setdiff1d(n2,n1))

# Addition of Numpy Arrays
# To get sum of the arrays both the arrays should have comaptible dimensions 
n1 = np.array([10, 20, 30, 40])
n2 = np.array([40, 50, 60, 70])
print(np.sum([n1,n2]))
print(np.sum([n1,n2],axis=0)) # Additon column-wise i.e 10+40 = 50
print(np.sum([n1,n2],axis=1)) # Additon row-wise i.e 10 + 20 + 30 + 40 = 100

# Scalar Operations on NumPy Arrays
n1 = np.array([10, 20, 30, 40])
n1=n1+1
print(n1)
n1 = np.array([10, 20, 30, 40])
n1=n1-2
print(n1)
n1 = np.array([10, 20, 30, 40])
n1=n1*2
print(n1)
n1 = np.array([10, 20, 30, 40])
n1=n1/10
print(n1)

# Mathematical Functions on Numpy array 
n1 = np.array([10, 20, 30, 40])
print(np.mean(n1))
print(np.std(n1))
print(np.median(n1))

# NumPy Matrix 
n =  np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print(n[0])
print(n[1])
print(n[:,1])
print(n[:,2])
# Transpose Matrix 
print(np.transpose(n))

# Matrix Multiplication
n1=np.array([[1,2,3],[4,5,6],[7,8,9]])
n2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(n1.dot(n2))
print(n2.dot(n1))

# Save and Load NumPy Array 
np.save('my_numpy',n1)

n2=np.load('my_numpy.npy')
print(n2)