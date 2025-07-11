# -*- coding: utf-8 -*-
"""Diabetes Prediction .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CD0o303DrdyfrlgBsmKUfWEGADBVlPVq
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

dip=pd.read_excel('/content/diabetes.xlsx')

dip.head()

dip.isnull().sum()

log=LogisticRegression()

a=dip[['preg','plas','pres','skin','insu','mass','pedi','age']]

b=dip['class']

log.fit(a,b)

preg=int(input('enter the preg'))
plas=int(input('enter the plas'))
pres=int(input('enter the pres'))
skin=int(input('enter the skin'))
insu=int(input('enter the insu'))
mass=float(input('enter the mass'))
pedi=float(input('enter the pedi'))
age=int(input('enter the age'))
ans=log.predict([[preg,plas,pres,skin,insu,mass,pedi,age]])
print(ans)

log.score(a,b)

from sklearn.metrics import accuracy_score

pvalu=log.predict(a)
accuracy_score(b,pvalu)