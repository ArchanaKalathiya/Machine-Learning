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




