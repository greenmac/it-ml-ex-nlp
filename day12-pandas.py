# https://ithelp.ithome.com.tw/articles/10191588
# https://www.kaggle.com/c/titanic
# https://github.com/GoatWang/ithome_ironman/blob/master/day12_pandas/PandasUsage_publish.ipynb
import pandas as pd
import numpy as np
from collections import Counter
import re

from sklearn import preprocessing

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

import seaborn as sns
sns.set()
# %matplotlib inline # 這段無法解決錯誤
import string

import os 
from datetime import datetime
import random
import math

from sklearn.model_selection import train_test_split

df = pd.read_csv('train.csv') #建立一個DataFrame。如果大家的train.csv不是跟執行的pythony在同一個資夾，請寄格更改路徑位置

# df.head(N) # N如果不填，則回傳頭5行

A = df['Cabin'][0]           #pandas中索引的方法後面會說，你只要知道這一個欄位是NaN就可以了
print(A)                     #nan
print(A == None)             #False
print(pd.isnull(A))          #True
print(pd.notnull(A))         #Fasle

A = np.nan
print(A)                     #nan
print(A == None)             #False
print(pd.isnull(A))          #True
print(pd.notnull(A))         #Fasle

A = None
print(A)                     #None
print(A == None)             #True
print(pd.isnull(A))          #True
print(pd.notnull(A))         #Fasle

df.head()

df.describe()

sns.pairplot(df[['Survived', 'Pclass', 'SibSp', 'Parch', 'Fare']])

colormap = plt.cm.viridis
plt.figure(figsize=(14,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(df[['Survived', 'Pclass', 'SibSp', 'Parch', 'Fare']].astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)

C_Cabins = []
for c in df['Cabin']:
#     if type(c) != float and c.startswith('B'):
    if pd.notnull(c) and c.startswith('B'):
        C_Cabins.append(c)
C_Cabins

plt.hist(df['Fare'])
plt.show()

print(len(df))
print(df.columns)
print(df.index)