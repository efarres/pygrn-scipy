# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data

df1 = data.get_data_yahoo('^DJI', '2015-01-01', '2018-01-01')
df1.head()


df2 = data.get_data_yahoo('^IXIC', '2015-01-01', '2018-01-01')
df2.head()


plt.plot(df1['Open'])
plt.plot(df2['Open'])
plt.grid(True)
plt.show()

fig, ax1 = plt.subplots()

ax1.plot(df1['Open'], color = 'blue', label = '^STOXX50E')
ax2= ax1.twinx()
ax2.plot(df2['Open'], color = 'red', label = 'AAPL')
ax1.legend()
ax2.legend()
plt.grid(True)
plt.show()

d1 = df1['Open']
d2 = df2['Open']

d1 = (d1 - d1.min()) / (d1.max() - d1.min())
d2 = (d2 - d2.min()) / (d2.max() - d2.min())

plt.plot(d1)
plt.plot(d2)
plt.grid(True)
plt.show()


d1_diff = np.diff(d1)
d2_diff = np.diff(d2)
plt.scatter(d1, d2)
plt.grid(True)
plt.show()

plt.hist(d1_diff, bins = 50, label = '^DJI', normed = True, range = [-.10, .10])
plt.hist(d2_diff, bins = 50, histtype = 'step', label = '^IXIC', normed = True, range = [-.10, .10])
plt.legend()
plt.grid(True)
plt.show()
