import numpy as np

arr = np.array([1,2,3,4,5,6,2,6,2,4,6])

# where()  Will search for value 4 in the array

locations = np.where(arr == 2)
print(locations)

# Will return the index locations where the values are EVEN

evenLocations = np.where(arr%2 ==0)

print(evenLocations)

# Will return the index locations where the values are ODD

oddLocations = np.where(arr%2 ==1)

print(oddLocations)

# searchsorted() performs binary search in the array and returns index where the specified value should be inserted

sortedArray = np.array([4,5,6,7,8,9])
valueToBeInsertedOnLocation = np.searchsorted(sortedArray, 5)
multipleValueToBeInsertedOnLocation = np.searchsorted(sortedArray, [2,5,6])

print(valueToBeInsertedOnLocation)
print(multipleValueToBeInsertedOnLocation)


