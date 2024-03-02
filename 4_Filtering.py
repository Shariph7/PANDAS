# Filtering in Pandas is just like a SQL Injections which needs the condition for the execution
# loc[] functions is used to filters in python pandas.

import pandas as pd
df = pd.read_csv('data.csv')

print(df.loc[df['Salary']>1000]) # Conditions
# Bitwise operators implementation.
print(df.loc[(df['gender'] == 'Male') & (df['Salary'] > 10000)])
# Best Examples of Filtering Data in Python Pandas.