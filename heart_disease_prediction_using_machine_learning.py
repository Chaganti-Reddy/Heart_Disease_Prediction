# -*- coding: utf-8 -*-
"""Heart_DIsease_Prediction_Using_Machine-Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nSH1QvdJkdoElz_hnzBF-S39xe1E0kas

# 1. Importing the Libraries
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import seaborn as sns
import joblib
from tkinter import *
import matplotlib.pyplot as plt

"""# 2. Importing Dataset """

data = pd.read_csv('heart.csv')

"""# 3. Taking care of Missing Values



"""

data.isnull().sum()

"""# 4. Taking care of Duplicate Values"""

data_dup = data.duplicated().any()

data_dup

data = data.drop_duplicates()

data_dup = data.duplicated().any()

data_dup

"""# 5. Data Processing"""

cate_val = [] # Columns which contains categorical values.
cont_val = [] # Columns which contains numerical values.

for column in data.columns :
  if data[column].nunique() <= 10 :
    cate_val.append(column)
  else :
    cont_val.append(column)

cate_val

cont_val

"""# 6. Encoding Categorical Data"""

cate_val

data['cp'].unique()

cate_val.remove("target")
cate_val.remove("sex")

# These colums are already contains 0's & 1's so no need of Encoding

data = pd.get_dummies(data, columns = cate_val, drop_first = True)

data.head()

"""# 7. Feature Scaling"""

st = StandardScaler()
data[cont_val] = st.fit_transform(data[cont_val])

data.head()

"""# 8. Splitting The Dataset Into Training Set and Test Set"""

X = data.drop("target", axis = 1)

Y = data["target"]

X_train , X_test, Y_train , Y_test = train_test_split(X,Y,test_size = 0.2, random_state=40)

X_train, Y_train

X_test, Y_test

"""# 9. Logistic Regression"""

data.head()

log = LogisticRegression()
log.fit(X_train, Y_train)

y_pred1 = log.predict(X_test)

accuracy_score(Y_test, y_pred1)

"""# 10. SVC (Support Vector Classifier)"""

svm = svm.SVC()

svm.fit(X_train, Y_train)

y_pred2 = svm.predict(X_test)
accuracy_score(Y_test, y_pred2)

"""# 11. KNeighbors Classifier"""

knn = KNeighborsClassifier()

knn.fit(X_train, Y_train)

y_pred3 = knn.predict(X_test)

accuracy_score(Y_test, y_pred3)

score = []

for k in range(1,49) :
  knn = KNeighborsClassifier(n_neighbors = k)
  knn.fit(X_train, Y_train)
  y_pred = knn.predict(X_test)
  score.append(accuracy_score(Y_test, y_pred))

score

plt.plot(score)
plt.xlabel("K Value")
plt.ylabel("Acc")
plt.show

knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(X_train, Y_train)
y_pred = knn.predict(X_test)
accuracy_score(Y_test, y_pred)

"""# Non-Linear ML Algorithms"""

data = pd.read_csv('heart.csv')
data.head()

data = data.drop_duplicates()
data.shape

X = data.drop('target', axis = 1)
Y = data['target']

X_train , X_test, Y_train , Y_test = train_test_split(X,Y,test_size = 0.2, random_state=42)

"""# 12. Decision Tree Classifier"""

dt = DecisionTreeClassifier()

dt.fit(X_train, Y_train)

y_pred4 = dt.predict(X_test)

accuracy_score(Y_test, y_pred4)

"""# 13. Random Forest Classifier"""

rf = RandomForestClassifier()

rf.fit(X_test, Y_test)

y_pred5 = rf.predict(X_test)

accuracy_score(Y_test, y_pred5)

"""# 14. Gradient Boosting Classifier"""

gbc = GradientBoostingClassifier()

gbc.fit(X_train, Y_train)

y_pred6 = gbc.predict(X_test)

accuracy_score(Y_test, y_pred6)

final_data = pd.DataFrame({'Models': ['LR','SVM','KNN','DT','RF','GB'],
                           'ACC':[accuracy_score(Y_test, y_pred1)*100,
                                  accuracy_score(Y_test, y_pred2)*100,
                                  accuracy_score(Y_test, y_pred3)*100,
                                  accuracy_score(Y_test, y_pred4)*100,
                                  accuracy_score(Y_test, y_pred5)*100,
                                  accuracy_score(Y_test, y_pred6)*100]})

final_data

sns.barplot(final_data['Models'], final_data['ACC'])

"""#### So Random Forest model gives a good accuracy so it is best model"""

X = data.drop("target", axis=1)
Y = data['target']

X.shape

rf = RandomForestClassifier()
rf.fit(X,Y)

"""# 15. Prediction on New Data"""

new_data = pd.DataFrame({
    'age': 52,
    'sex' : 1,
    'cp' : 0,
    'trestbps' : 125,
    'chol' : 212,
    'fbs' : 0,
    'restecg' : 1,
    'thalach' : 168,
    'exang' : 0,
    'oldpeak' : 1.0,
    'slope' : 2,
    'ca' : 2,
    'thal' : 3,
}, index=[0])

new_data

p = rf.predict(new_data)
if p[0] == 0:
  print("No Disease")
else :
  print("Suffering from Disease")

"""# 16. Save Model Using Joblib"""

joblib.dump(rf, 'model_joblib_heart')

model = joblib.load('model_joblib_heart')

model.predict(new_data)

"""# GUI"""

def show_entry_fields():
    p1=int(e1.get())
    p2=int(e2.get())
    p3=int(e3.get())
    p4=int(e4.get())
    p5=int(e5.get())
    p6=int(e6.get())
    p7=int(e7.get())
    p8=int(e8.get())
    p9=int(e9.get())
    p10=float(e10.get())
    p11=int(e11.get())
    p12=int(e12.get())
    p13=int(e13.get())
    model = joblib.load('model_joblib_heart')
    result=model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p8,p10,p11,p12,p13]])
    
    if result == 0:
        Label(master, text="No Heart Disease").grid(row=31)
    else:
        Label(master, text="Possibility of Heart Disease").grid(row=31)


master = Tk()
master.title("Heart Disease Prediction System")


label = Label(master, text = "Heart Disease Prediction System"
                          , bg = "black", fg = "white"). \
                               grid(row=0,columnspan=2)


Label(master, text="Enter Your Age").grid(row=1)
Label(master, text="Male Or Female [1/0]").grid(row=2)
Label(master, text="Enter Value of CP").grid(row=3)
Label(master, text="Enter Value of trestbps").grid(row=4)
Label(master, text="Enter Value of chol").grid(row=5)
Label(master, text="Enter Value of fbs").grid(row=6)
Label(master, text="Enter Value of restecg").grid(row=7)
Label(master, text="Enter Value of thalach").grid(row=8)
Label(master, text="Enter Value of exang").grid(row=9)
Label(master, text="Enter Value of oldpeak").grid(row=10)
Label(master, text="Enter Value of slope").grid(row=11)
Label(master, text="Enter Value of ca").grid(row=12)
Label(master, text="Enter Value of thal").grid(row=13)



e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)
e12 = Entry(master)
e13 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
e10.grid(row=10, column=1)
e11.grid(row=11, column=1)
e12.grid(row=12, column=1)
e13.grid(row=13, column=1)



Button(master, text='Predict', command=show_entry_fields).grid()

mainloop()