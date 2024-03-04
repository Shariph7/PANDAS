# DataFrame is the collections of the Series which is uses to holds the 2 dimensionals values.

# DataFrame Sorting
import pandas as pd
dict = {
    'Emp' : ['Shariph','Suraj','Sapana'],
    'Age' : [17,18,16]
}
df = pd.DataFrame(dict)
print(df.sort_index(ascending=True))
print(df.sort_index(ascending=False))


# Drop Duplicates values from the pandas
print('---------Duplication------------')
import pandas as pd
dict = {
    'Emp' : ['Shariph','Suraj','Sapana','Suraj'],
    'Age' : [17,18,16,18]
}
df = pd.DataFrame(dict)
# To check the Duplicated Values.
print(df.duplicated())
print(df.drop_duplicates()) # This will deletes the Duplicated Values.

# Slicing DataFrame in pandas
df = pd.read_csv('Data.csv')
# Head Method.
print(df.head()) # gives the data of first 5 rows as default.
print(df.tail()) # gives the data of last five rows as default.