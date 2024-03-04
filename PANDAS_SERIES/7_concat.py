# Concatinating the DataFrame in Python Pandas
# concat() functions concat the dataFrame

import pandas as pd
df1 = pd.DataFrame({'emp_name':['Shariph','Himal','Krishna'],
                    'Age':[17,28,18]})
df2 = pd.DataFrame({'emp_name':['Shariph','Himal','Ravi'],
                    'Salary(Per Month in Lakhs)':[15,2,5]})

df = pd.concat([df1,df2], ignore_index=True)
# axis = 1 For the vertical Representation of Data.
# Concat() requires the data in the form of lists.
print(df)