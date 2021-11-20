# categorical data to numerical data
# OrdinalEncoder is for 2D data with the shape(n_samples, n_features)
# LabelEncoder is for 1D data with the shape(n_samples,))
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

df = pd.DataFrame.from_dict({'Name': ['Tom', 'nick', 'krish', 'jack'],
                             'Age': [20, 21, 19, 18],
                             'Education': ['BA', 'Bsc', 'BE', 'Bcom'],
                             'Salery': [1, 2, 3, 4]
                             })

# from sklearn.preprocessing import OrdinalEncoder
ord_enc = OrdinalEncoder()
df["ocean_proximity"] = ord_enc.fit_transform(df[["ocean_proximity"]])
# ord_enc.fit_transform(df)  even encoding entire df is possible
