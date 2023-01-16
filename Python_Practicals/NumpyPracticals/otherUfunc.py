import numpy as np

arr = np.array([4, 23, 58, 92])

newArr = np.diff(arr) # Find difference b/w elements

newArr2 = np.diff(arr,n=2) # This operation will be repeated n times

lcmAns = np.lcm(12,14) # LCM between two numbers

lcmArr = np.lcm.reduce(arr)
lcmBwMulNumbers = np.lcm.reduce(np.arange(1,11))

# -------Finding GCD--------

arr = np.array([20, 8, 32, 36, 16])

gcdAns = np.gcd.reduce(arr)


#------------Trigo Functions-------------
sinArr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

sinOnArr = np.sin(sinArr)
sin = np.sin(np.pi/2)

# Degree to Radians (vice-versa)

degreeArr = np.array([90, 180, 270, 360])
radiansArr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])


radians = np.deg2rad(degreeArr)
degrees = np.rad2deg(radiansArr)

#-------------Hypotenues----------

base =3
prep =4

hyp = np.hypot(base,prep)


print(newArr)
print(newArr2)
print(lcmAns)
print(lcmArr)
print(lcmBwMulNumbers)
print(gcdAns)
print(sin)
print(sinOnArr)
print(degrees)
print(radians)
print(hyp)