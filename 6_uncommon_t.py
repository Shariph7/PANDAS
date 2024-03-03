# Pandas DataFrame Having Uncommon Data or Table name

import pandas as pd
df1 = pd.DataFrame({'emp_name':['Shariph','Himal','Krishna'],
                    'Age':[17,28,18]})
df2 = pd.DataFrame({'citizen':['Shariph','Himal','Ravi'],
                    'Salary(Per Month in Lakhs)':[15,2,5]})

# Merging the table having no common table name
print("-----------------------Inner Join---------------------")
print(pd.merge(df1,df2,  left_on='emp_name', right_on='citizen', how='inner'))

print("-----------------------Right Join---------------------")
print(pd.merge(df1,df2,  left_on='emp_name', right_on='citizen', how='right'))

print("-----------------------Left Join---------------------")
print(pd.merge(df1,df2,  left_on='emp_name', right_on='citizen', how='left'))

print("-----------------------Outer(Full) Join---------------------")
print(pd.merge(df1,df2,  left_on='emp_name', right_on='citizen', how='outer'))