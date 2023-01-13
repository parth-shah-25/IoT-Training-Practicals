import numpy as np ,time,sys


SIZE = 100000

list1 = range(SIZE)
list2 = range(SIZE)

numpyArray1 = np.arange(SIZE)
numpyArray2 = np.arange(SIZE)

start = time.time()

# For Lists
result = [(x,y) for x,y in zip(list1, list2)]  
print((time.time() - start)*1000, "ms")

start = time.time()

# For Numpy Array
result = numpyArray1 + numpyArray2
print((time.time() - start)*1000, "ms")