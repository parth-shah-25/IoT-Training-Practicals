import pandas as pd, numpy as np
from openpyxl.workbook import Workbook

animalVisitData = {'animal':['cat','cat','dog','lion','Tortoise','snake','tiger'],
                    'age': [2,4,3,6,np.NaN,5,1],
                    'visits': [4,7,2,9,7,15,61]}

labels = ['a','b','c','d','e','f','g']

animalVisitDataFrame = pd.DataFrame(animalVisitData,index=labels)

# CSV FILE ---------------

animalVisitDataFrame.to_csv('animal_visits.csv')

csv_animal = pd.read_csv('animal_visits.csv')

print(csv_animal)
