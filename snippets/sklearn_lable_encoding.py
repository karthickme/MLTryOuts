# categorical data to numerical data
# OrdinalEncoder is for 2D data with the shape(n_samples, n_features)
# LabelEncoder is for 1D data with the shape(n_samples,))
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame.from_dict({"lang": ['Python', 'Java', 'Python', 'Python',
                                      'C++', 'C++', 'Java', 'Python', 'C++', 'Java']})


# from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(df.lang)
df['label_enided'] = integer_encoded

print(df)
