# Kfold to split the data and perform high levle check.
from sklearn.model_selection import StratifiedKFold, cross_val_score
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

df = pd.DataFrame.from_dict({'Name': ['Tom', 'nick', 'krish', 'jack'],
                             'Age': [20, 21, 19, 18],
                             'Education': ['BA', 'Bsc', 'BE', 'Bcom'],
                             'income': [1, 2, 3, 4]
                             })

X = df.drop("income")
Y = df.income

model = DecisionTreeRegressor()

# from sklearn.model_selection import StratifiedKFold, cross_val_score
# model = XXXXX()
kfold = StratifiedKFold(n_splits=10)
# cv=10 to go raw with cross_valdiation when calling cross_val_score function
results = cross_val_score(model, X, Y, cv=kfold)
