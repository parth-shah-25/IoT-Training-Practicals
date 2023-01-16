from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------NORMAL DISTRIBUTIONS-------------

# random.normal(loc(Mean), scale(Standard Deviation), size(Shape of the Returned array))

x = random.normal(loc=1, scale=2,size=(2,3))

# sns.distplot(random.normal(size=100), hist = False)

# print(x)
# plt.show()


# ---------------BIONOMIAL DISTRIBUTIONS-------------

bionomialDist = random.binomial(n=10, p=0.5, size=10)

# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

print(bionomialDist)
# plt.show()


# ---------------POISSON DISTRIBUTIONS-------------

poissonDist = random.poisson(lam=2, size=10)

# sns.distplot(random.poisson(lam=2, size=1000), kde=False)

# print(poissonDist)
# plt.show()