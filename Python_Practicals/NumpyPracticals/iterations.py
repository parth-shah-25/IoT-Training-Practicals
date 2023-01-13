import numpy as np

arr = np.array([[1,2,3,4],[1,2,3,4]])

print(arr)

# For 2-D Array
for i in arr:
    for j in i:
        print(j)


arr2 = np.array([[[1,2,3,4],[5,6,7,8]]])

print(arr2)

for i in arr2:
    for j in i:
        for k in j:
            print(k)