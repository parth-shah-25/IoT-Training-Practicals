from numpy import random


# Generates an array with the elements from the mentioned array with mentioned probability in p=[]  (PROBABILITY FOR EVERY ELEMENT MUST BE MENTIONED)
x = random.choice([3,4,5,6,7], p=[0.3,0.3,0.1,0.2,0.1], size=(10))
print(x)

# Generates 2-D array
x = random.choice([3,4,5,6,7], p=[0.3,0.4,0.1,0.1,0.1], size=(2,4))
print(x)