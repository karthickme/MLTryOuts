import pandas as pd

tables = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')


df = tables[0]
df = df[['Country or dependent territory', 'Region', 'Population']]

# mean of all the columnes in the df
# df.mean()

# min of all the columns in the df
# df.min()

# max of all the columns in the df
# df.min()

# describe the df
# df.describe()

# info of the dataframe
# df.info()

# ==================================

df.drop_duplicates()


# fill nan values with Mean/median/mode
df.fillna(df.mean())

# clip the data range between a ranchage or 0 to 1000

df['new_range'] = df['range'].clip(0, 60)
