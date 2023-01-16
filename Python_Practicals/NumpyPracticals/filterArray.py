import numpy as np

arr = np.array([1,5,2,8,4])

filteredArray = []

for element in arr:
    if(element > 2):
        filteredArray.append(True)
    else:
        filteredArray.append(False)

newArray = arr[filteredArray]

print(filteredArray)
print(newArray)

# FOR EVEN ELEMENTS USING FILTERING
filteredArray = []
for element in arr:
    if(element%2 == 0):
        filteredArray.append(True)
    else:
        filteredArray.append(False)

print(filteredArray)
evenArray = arr[filteredArray]

print(evenArray)