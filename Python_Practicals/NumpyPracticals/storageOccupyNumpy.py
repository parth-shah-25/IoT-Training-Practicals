import numpy as np ,time,sys



values = range(1000)

print(sys.getsizeof(4)*len(values))

# Numpy occupies less storage than standard list
numpyArray = np.arange(1000)

print(numpyArray.size*numpyArray.itemsize)
