import numpy as np

array = np.array([],dtype='int64')

for i in range(0,10):
    value = input("Enter value:")
    array = np.insert(array, i,value)

print(array)

print("Length of the array is: ",array.size)

sum=0
for ele in array:
    sum = sum + ele


print("Reverse of the array:",np.flip(array))
print("Sum of the Array: ",sum)