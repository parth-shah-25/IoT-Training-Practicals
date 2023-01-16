import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
forAbs = np.array([1,-2,-3,4,-5])

arrAdd = np.add(x,y)
arrSub = np.subtract(x,y)
arrMul = np.multiply(x,y)
arrDiv = np.divide(x,y)
arrPow = np.power(x,y)
arrMod = np.mod(x,y)  # or arrMod = np.reminder(x,y)  
arrDivMod = np.divmod(x,y)
arrAbs = np.absolute(forAbs)

#---------------Cummulative Sum----------------
# x = [1,2,3,4] i.e. [1,1+2,1+2+3,1+2+3+4]

arrCummulativeSum = np.cumsum(x)

#---------------Cummulative Product----------------
# x = [1,2,3,4] i.e. [1,1*2,1*2*3,1*2*3*4]

arrCummulativeProd = np.cumprod(x)

#---------------Product------------------
arrProduct = np.prod([x,y])

print(arrAdd)
print(arrSub)
print(arrMul)
print(arrDiv)
print(arrPow)
print(arrMod)
print(arrDivMod)
print(arrAbs)
print(arrCummulativeSum)
print(arrCummulativeProd)
print(arrProduct)