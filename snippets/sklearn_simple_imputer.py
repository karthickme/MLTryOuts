# filling the missing values in a col
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd


df = {'Name': ['Tom', 'nick', 'krish', 'jack'],
      'Age': [20, 21, np.NaN, 18],
      'Education': ['BA', 'Bsc', 'BE', 'Bcom'],
      'Salery': [1, 2, 3, 4]
      }


# from sklearn.impute import SimpleImputer
col = df.columns
# strategy can be mean , median  “most_frequent” or constant
mean_imputer = SimpleImputer(strategy='median')

result_mean_imputer = mean_imputer.fit_transform(df)

df = pd.DataFrame(result_mean_imputer, columns=col)
