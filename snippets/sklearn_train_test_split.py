# Splitting data for training and testing
from pandas import pd
from sklearn.model_selection import train_test_split

df = pd.DataFrame.from_dict({'Name': ['Tom', 'nick', 'krish', 'jack'],
                             'Age': [20, 21, 19, 18],
                             'Education': ['BA', 'Bsc', 'BE', 'Bcom'],
                             'Salery': [1, 2, 3, 4]
                             })

# from sklearn.model_selection import train_test_split
y = df.median_house_value
X = df.drop('median_house_value', axis=1)

# going with 80:20 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)  # , random_state=100)
