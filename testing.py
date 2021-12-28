# %%
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
# %% 

df = pd.read_csv('Tuesday-2019-Stats.csv')
print(df)
print (df.max())
print (df.min())

print(df.mean())
cols = ['Gm1', 'Gm2', 'Gm3']
print (df[cols].mean())
chart = df[cols].mean().plot(kind='bar')
for data in df:
    print (data)


print (chart)
df[cols].mean().hist()

# %%
