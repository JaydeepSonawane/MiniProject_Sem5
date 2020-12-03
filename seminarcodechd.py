# -*- coding: utf-8 -*-
"""SeminarCodeCHD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/163yuoeWxxfATRIoWMptdgdaSpiKDdqIs
"""

import pandas as pd

df = pd.read_csv('/content/cleveland.csv', header = None)


df.columns = ['age', 'gender', 'cp', 'trestbps', 'chol',
              'fbs', 'restecg', 'thalach', 'exang', 
              'oldpeak', 'slope', 'ca', 'thal', 'CHD']

df.head(10)

df.isnull().sum()

df['CHD'] = df.CHD.map({0: 0, 1: 1, 2: 1, 3: 1, 4: 1})
df['gender'] = df.gender.map({0: 'female', 1: 'male'})
df['thal'] = df.thal.fillna(df.thal.mean())
df['ca'] = df.ca.fillna(df.ca.mean())

import matplotlib.pyplot as plt
import seaborn as sns


# distribution of CHD vs age 
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 20}) 
sns.catplot(kind = 'count', data = df, x = 'age', hue = 'CHD', order = df['age'].sort_values().unique())
plt.title('Variation of Age for each target class')
plt.show()

#barplot of age vs sex with hue = target
sns.catplot(kind = 'bar', data = df, y = 'age', x = 'gender', hue = 'CHD')
plt.title('Distribution of age vs gender with the CHD class')
plt.show()

df['gender'] = df.gender.map({'female': 0, 'male': 1})

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler as ss
sc = ss()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
result=classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm_test = confusion_matrix(y_pred, y_test)

y_pred_train = classifier.predict(X_train)
cm_train = confusion_matrix(y_pred_train, y_train)

from sklearn.metrics import accuracy_score
predictions = result.predict(X_test)
accuracy_score(y_test,predictions)

"""Prediction of New Values :
requires 13 values : age | gender | chestPain | restBP | cholestoral | fastbloodSugar | restECG | MaxHeartRate | exerciseInduceAngina |
                     oldpeak | slopeSTsegmnt | ca | thal
pred_new = classifier.predict([[ , , , , , , , , , , , , ]]) 
pred_new     #Here 0 : No CHD , 1 : CHD
"""

pred_new = classifier.predict([[ 41, 0,2 ,130 ,204 ,0 ,2 ,172 ,0 ,1.4 ,1 ,0.0 ,3.0 ]])
pred_new

pred_new = classifier.predict([[53,	1,	4,	140,	203,	1,	2	,155	,1	,3.1,	3	,0.0	,7.0	]])
pred_new