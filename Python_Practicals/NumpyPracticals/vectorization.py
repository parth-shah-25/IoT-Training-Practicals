import numpy as np

x = [1,2,3,4,5]
y = [6,7,8,9,10]
z=[]

# Without using ufunc, zip() is used..

# for i,j in zip(x,y):
#     z.append(i+j)

# print(z)

# # With ufunc, add(list1, list2) is used...

# numpyAdd = np.add(x, y)
# print(numpyAdd)

# Creating our own ufunc using frompyfunc(function,inputs,outputs)

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd,2,1)

print(myadd(x,y))