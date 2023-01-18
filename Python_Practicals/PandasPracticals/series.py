import pandas as pd, numpy as np

# Series Create, Manipulate, Query, Delete

arr = [0,1,2,3,4]
series1 = pd.Series(arr)
# print(series1)


# Series with index order mentioned by the User
differentIndexOrder = [1,2,3,4,5]
series2 = pd.Series(arr, index=differentIndexOrder)

# print("Series with index order mentioned by the User:")
# print(series2)

numpyArray = np.random.randn(5)
customIndex = ['a','b','c','d','e']
series3 = pd.Series(numpyArray, index=customIndex)
# print(series3)

# --------Creating Series from a dictionary--------------
dictionary = {'a':1,'b':2,'c':3,'d':4,'e':5}
series4 = pd.Series(dictionary)
# print(series4)


#------------------MODIFYING---------------

series1.index = ['A','B','C','D','E'] # Changed Index of Series 1
# print(series1)


# -----Slicing--- 

slicedSeries1 = series1[:3]
slicedSeries2 = series1[:-1]
# print(slicedSeries1)
# print(slicedSeries2)



# --- Combining a series to another---

# combinedSeries = series1.append(series3)  # OLD WAY
combinedSeries = pd.concat([series1,series3])  # NEW WAY
# print(combinedSeries)



#----Dropping a row
#---------------(THESE CHANGES WILL BE TEMPERORY)

#   To Change -----
# combinedSeries = combinedSeries.drop('e')
# print(combinedSeries.drop('e'))


#--------------------SERIES OPERATIONS--------------------------

# Addition to another series--------------

arr1= [0,1,2,3,4,5]
arr2 = [9,7,6,5,4,3,2,1]

toAddSeries1 = pd.Series(arr1)
toAddSeries2 = pd.Series(arr2)
# print(toAddSeries1.add(toAddSeries2))



# Subtraction to another series--------------

print(toAddSeries1.sub(toAddSeries2))


# Multiplication to another series--------------

print(toAddSeries1.mul(toAddSeries2))


# Division to another series--------------

print(toAddSeries1.div(toAddSeries2))


# Min / Max / Median------------------

# *** Median drops infinity / NaN values while computing

print('Min: ',toAddSeries1.min())
print('Max: ',toAddSeries1.max())
print('Median: ',toAddSeries1.median())