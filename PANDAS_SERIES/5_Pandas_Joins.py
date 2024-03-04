# Python Pandas Joins.
import pandas as pd
df1 = pd.DataFrame({'emp_name':['Shariph','Himal','Krishna'],
                    'Age':[17,28,18]})
df2 = pd.DataFrame({'emp_name':['Shariph','Himal','Ravi'],
                    'Salary(Per Month in Lakhs)':[15,2,5]})

# Default Joins is inner Joins
# Default is inner joins which will display the values of the table having common values.
print('------------------Inner Join---------------------')
print(pd.merge(df1,df2))

# Right Joins - Gives the values of the right table only.
print('------------------Right Join---------------------')
print(pd.merge(df1,df2,on='emp_name', how='right'))

# Left Joins - Gives the values of the left table only.
print('------------------Left Join---------------------')
print(pd.merge(df1,df2, on='emp_name', how='left'))

# Outer Join(Full Join) - Gives the values of the both tables.
print('------------------OuterJoin---------------------')
print(pd.merge(df1,df2, on='emp_name', how='outer'))