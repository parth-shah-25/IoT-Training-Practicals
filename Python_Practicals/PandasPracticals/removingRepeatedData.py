import pandas as pd, numpy as np

df = pd.DataFrame({'A': [1,2,2,2,3,4,4,5,6,7,8,8,9]})
print(df.loc[df['A'].shift() != df['A']])  # Removes Duplicates