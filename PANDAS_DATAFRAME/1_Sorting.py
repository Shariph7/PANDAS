# PANDAS DATAFRAME SORTING
import pandas as pd
df = pd.read_csv('G:\GIT-GITHUB\PANDAS_IN_PYTHON\PANDAS_DATAFRAME\data.csv')
print(df.sort_index(ascending=True))
print('-------------------------------------------------------------------------------------------------')
print(df.sort_index(ascending=False))


# Duplicated Values in the DataFrame!
print(df.duplicated()) # shows how many data is being dulicted in th dataframe.
print(df.drop_duplicates())

# Slicing in Pandas DataFrame
print(df.head())
print(df.tail())