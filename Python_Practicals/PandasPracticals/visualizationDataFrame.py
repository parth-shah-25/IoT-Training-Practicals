import pandas as pd, numpy as np, matplotlib.pyplot as plt


ts = pd.Series(np.random.randn(50),index=pd.date_range('today', periods=50))

ts = ts.cumsum()
# ts.plot()


df = pd.DataFrame(np.random.randn(50,4), index=ts.index, columns=['A','B','X','Y'])

df =df.cumsum()
df.plot()
plt.show()