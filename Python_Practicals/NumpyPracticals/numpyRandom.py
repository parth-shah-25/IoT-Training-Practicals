from numpy import random

# Generates a random int value
randomInt = random.randint(100)
print(randomInt)


# Generates a random float value [DEFAULT]
randomFloat = random.rand()
print(randomFloat)
print(round(randomFloat,2))  # Prints only 2 decimal after float


# Generates 1-D Array
randomArray = random.randint(100,size=(10))
print(randomArray)


# Generates 2-D Array
randomTwoDArray = random.randint(100,size=(2,4))
print(randomTwoDArray)


# Generates random float array
floatArray = random.rand(5)
print(floatArray)
print()


# Generates random 2-D Array
floatTwoArray= random.rand(2,5)
print(floatTwoArray)


# Prints a random choice from mentioned array
randomChoice = random.choice(randomArray)
print(randomChoice)



# Generates a 1-D array that contains random value from the mentioned array
randomChoiceOneDArray = random.choice(randomArray,size=(4))
print(randomChoiceOneDArray)


# Generates a 2-D array that contains random value from the mentioned array
randomChoiceTwoDArray = random.choice(randomArray,size=(2,4))
print(randomChoiceTwoDArray)