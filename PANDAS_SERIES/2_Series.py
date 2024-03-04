# Python Pandas - Series
# Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# Importing Pandas Modules.
import pandas as pd
dict = [1,2,3,4]
df = pd.Series(dict)
print(df)

# Python Pandas Series Properties.
import pandas as pd
mylist = [10,20,30]
# Index
df = pd.Series(mylist, index=['a','b','c'])
# Name
df = pd.Series(mylist, index=['a','b','c'], name='My series')
print(df.size)
print(df.nbytes)
print(df.memory_usage)
print(df.empty)
# Size
print(df)