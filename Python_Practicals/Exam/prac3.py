import numpy as np

array = np.array([[2,4,6],[7,9,30]])

# Reshaping
tempArray = array.reshape(3,2)

print("Reshaping the Array:")
print(tempArray)


# Slicing
print("Slicing the Array:")
print(array[0,2])
