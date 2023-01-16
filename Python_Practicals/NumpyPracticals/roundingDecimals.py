import numpy as np

arr = np.trunc([-1.43232,1.43232]) # Truncation
print(arr)


arr = np.around(1.43232,2) # Rounding
print(arr)


arr = np.floor([1.43232,-1.43232]) # Floor (Rounds up to nearest lower integer)
print(arr)

arr = np.ceil([1.43232,-1.43232]) # ceil (Rounds up to nearest upper integer)
print(arr)
