# Kfold to split the data and perform high levle check.
from sklearn.model_selection import cross_val_score
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import pickle

df = pd.DataFrame.from_dict({'Name': ['Tom', 'nick', 'krish', 'jack'],
                             'Age': [20, 21, 19, 18],
                             'Education': ['BA', 'Bsc', 'BE', 'Bcom'],
                             'income': [1, 2, 3, 4]
                             })

X = df
Y = df.income

model = DecisionTreeRegressor()

results = cross_val_score(model, X, Y, cv=1)

pickle.dump(model, open('result.dat', 'wb'))
