# https://ithelp.ithome.com.tw/articles/10191616
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

df.loc[0]

df['Fare']

df.loc[[2,5,7]]

df.loc[0, 'Fare']

df.loc[[0,1,2], 'Fare']

df.loc[range(3), ['Fare','Cabin']]

df.loc[pd.isnull(df['Cabin'])]

df.loc[df['Sex']=='male']

df.loc[df['Age']> 70]

indexing_bool_list = np.random.randint(0,2,size=len(df)) == 1 #我們首先先創造出一個，隨機的、只有True跟False的、與df等長的list
print(indexing_bool_list[:30]) #看一下它前30個長什麼樣
df.loc[indexing_bool_list]  #然後我們看看DataFrame會如何反應

print(len(pd.isnull(df['Cabin'])), Counter(pd.isnull(df['Cabin'])))
print(len(df['Sex']=='male'), Counter(df['Sex']=='male'))
print(len(df['Age']> 70), Counter(df['Age']> 70))

columns = df.columns
df.columns = range(len(df.columns))
df.head(2)

df.columns = columns
df.head(2)

df.loc[df['Sex']=='male', 'Sex'] = 1
df.loc[df['Sex']=='female', 'Sex'] = 0
df.head(2)

df['Age'].describe()

std = df['Age'].std()
mean = df['Age'].mean()
size = len(df[pd.isnull(df['Age'])])
age_null_random_list = np.random.randint(mean - std, mean + std, size=size)
df.loc[pd.isnull(df['Age']), 'Age'] = age_null_random_list
df['Age'].describe()

num_NonSurvived = df.groupby('Survived').count()['PassengerId'][0]  # 死亡者的個數
num_Survived = df.groupby('Survived').count()['PassengerId'][1]  # 生還者的個數
duplicate_length = num_NonSurvived - num_Survived
print(num_NonSurvived)
print(num_Survived)
print(duplicate_length)

duplicate_indices = np.random.choice(df[df['Survived'] == 1].index, duplicate_length)  #choice可以直接幫你從一個list中，隨機挑選出指定size的item。這便則可以挑選出，特定size的index值。
df_duplicate = df.loc[duplicate_indices].copy()  # 索引出隨機挑選的index的row
print(len(df))
df = pd.concat([df, df_duplicate], ignore_index=True)  # 把挑選出來要負的的row，新增上原本的DataFrame
print(len(df))
df

df['Name_Length'] = 0 # 先透過這種方式新增好欄位做準備，下面執行效能會好很多
def cal_namelength(row):
    if pd.notnull(row['Name']):
        row['Name_Length'] = len(row['Name'])
    else:
        row['Name_Length'] = 0
    return row
df = df.apply(cal_namelength, axis=1)  # 記得: 1.要把新的df指派給原本的df才會成功更新。 2. axis要設定為1，才會以row為單位跑回圈。
df

df['Age_cat'] = 0
for idx, row in df.iterrows():  # 請務必記得加上idx，不然跑回圈的item會變成(idx, row)
    Age = row['Age']
    if Age < 20.315:
        Age_cat = 0
    elif Age < 40.21:
        Age_cat = 1
    elif Age < 60.1049:
        Age_cat = 2
    else:
        Age_cat = 3
    df.loc[idx, 'Age_cat'] = Age_cat
df

df.drop(['Age_cat', 'Name_Length'], axis=1, inplace=True)
df

df_line0 = df.loc[:2].copy()
print(len(df))
df.drop(range(3), inplace=True)
print(len(df))
df = pd.concat([df, df_line0], ignore_index=True)
print(len(df))

df['Age_cat'] = 0
for idx, row in df.iterrows():  # 請務必記得加上idx，不然跑回圈的item會變成(idx, row)
    Age = row['Age']
    if Age < 20.315:
        Age_cat = 0
    elif Age < 40.21:
        Age_cat = 1
    elif Age < 60.1049:
        Age_cat = 2
    else:
        Age_cat = 3
    df.loc[idx, 'Age_cat'] = Age_cat
df

df.groupby('Age_cat').count()

df.groupby('Age_cat').mean()

df.groupby('Age_cat').std()

df.groupby('Age_cat').median()

df.sort_values('Age', ascending=False)

from string import punctuation
from collections import Counter
df_name = df[['Name']]
def processname(name):
    if type(name) == str:
        for pun in punctuation:
            name = name.replace(pun, " ")
        terms = [term for term in name.split() if term != " "]
        return terms
    else:
        return []
df_name['processed'] = df['Name'].apply(processname)
df_name

all_terms = []
for terms in df_name['processed']:
    all_terms.extend(terms)
sorted(dict(Counter(all_terms)).items(), key=lambda x:x[1], reverse=True)

import matplotlib.pyplot as plt
from wordcloud import WordCloud

wordcloud = WordCloud()
wordcloud.generate_from_frequencies(frequencies=dict(Counter(all_terms)))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()