import pandas as pd, numpy as np


# Getting dates from today to 6 upcoming days ---------------

dates = pd.date_range('today', periods=6)
# print(dates)


# DataFrame from a List / Numpy Array--------------

numpyArray = np.random.randn(6,4)
columns = ['A','B','C','D']

dataFrame1 = pd.DataFrame(numpyArray,index=dates, columns=columns)
print(dataFrame1) 


# DataFrame from a dictionary


animalVisitData = {'animal':['cat','cat','dog','lion','Tortoise','snake','tiger'],
                    'age': [2,4,3,6,np.NaN,5,1],
                    'visits': [4,7,2,9,7,15,61]}

labels = ['a','b','c','d','e','f','g']

animalVisitDataFrame = pd.DataFrame(animalVisitData,index=labels)

# print(animalVisitDataFrame)


# print(animalVisitDataFrame.head())  # [DEFAULT] Prints first 5 entries
# print(animalVisitDataFrame.head(3))  #  Prints first n entries


# print(animalVisitDataFrame.tail())  # [DEFAULT] Prints last 5 entries
# print(animalVisitDataFrame.tail(3))  #  Prints last n entries

# Gives basic description of the data

# print(animalVisitDataFrame.describe())


# Sorting DataFrame---------------

# print(animalVisitDataFrame.sort_values(by='age'))


# Slicing the DataFrame -------------------

# print(animalVisitDataFrame[1:5])

# Slicing + Sorting ----------

# print(animalVisitDataFrame.sort_values(by='age')[1:5])


# ------------------------------- QUERY THE DATAFRAME BY TAG---------------------

# print(animalVisitDataFrame[['age','visits']])


# *** Modifiying the values in the DataFrame

animalVisitDataFrame.loc['f','age']= 3.0

# print(animalVisitDataFrame)



# -------------------------------- OPERATIONS ON MISSING VALUES IN DATAFRAME----------


# Copying the DF

copy_DF_Animal_Data = animalVisitDataFrame.copy()

# print(copy_DF_Animal_Data)

# Filling the NaN values with user defined values --------------

# print(copy_DF_Animal_Data.fillna(0))


copy2 = animalVisitDataFrame.copy()
# print(copy2)

# Dropping the NaN values -------------

print(copy2.dropna(how='any'))