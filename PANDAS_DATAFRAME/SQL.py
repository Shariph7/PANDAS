# SQL QUERIES IMPLEMENTATION IN PYTHON PANDAS.
import pandas as pd
df = pd.read_csv('G:\GIT-GITHUB\PANDAS_IN_PYTHON\PANDAS_DATAFRAME\data.csv')
# print(df)
# Select * from Table_Name limit;

# SQL - Select * from Table_Name limit;
print(df.head())
print(df.tail())

# Condtion(SQL) Select * from Table_Name Where age == 30;
print(df[df['Sale Prize'] ==' $20.00'])