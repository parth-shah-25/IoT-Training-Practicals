import numpy as np

array = np.array([1,2,3])

print(array.ndim,"D")  # To find te dimension of the array

print(array.itemsize) # To print the byte size (size occupied by each element in the array)

print(array.dtype) # To print the datatype of the item

a =np.array([(1,2,3,6),(1,3,3,4),(5,7,3,1)])  
print(a.size) # Prints Size of an array

# Reshaping-----------------
print(a.shape) # Prints shape of an array
print("Before Reshaping:\n", a)
# print("After Reshaping:\n",a.reshape(4,2)) # Reshapes the array

# Slicing ---------------------

# a =np.array([(1,2,3,6),(1,3,3,4),(5,7,3,1)])  

#                 [0]       [1]
print(a[0,2]) # Will print 3 as 3 is present on the 2nd position of the 0th element   

print(a[0:2,1]) # Will print the 1st item of the first two elements

# Linespacing---------------
print("Lienspacing:\n")
print(np.linspace(1,3,5))

# Min / Max / Sum

a = np.array([1,2,3,4,5]) 

print(a.max())
print(a.min())
print(a.sum())

# Axis=1 is Row  || Axis=0 is Column---------

a =np.array([(1,2,3,6),(1,3,3,4)])  

print(a)
print(a.sum(axis=0)) # Sum of elements in column
print(a.sum(axis=1)) # Sum of elements in row

print(np.sqrt(a))  # Prints Square root of every element in the array

print(np.std(a)) # Prints Standard Deviation

# Matrix + , - , / , * 

a =np.array([(1,2,3,4),(5,6,7,8)])  
b =np.array([(1,2,3,6),(1,3,3,4)])  

print("Addition:\n",a+b)
print("Subtraction:\n",a-b)
print("Multiplication:\n",a*b)
print("Division:\n",a/b)

# Concatinating two matrices------------------

# Vertical Scaling----

print(np.vstack((a,b)))
print(np.hstack((a,b))) 

print(a.ravel()) # Prints elements in single line