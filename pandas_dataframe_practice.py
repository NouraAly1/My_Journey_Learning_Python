'''
This is a practice file for learning pandas DataFrame operations.
Most code is commented out as examples for reference.
'''

import pandas as pd

'''Reading Excel file and basic DataFrame operations: selecting columns, using iloc and loc'''
df = pd.read_excel('employee.xlsx')
#print(df)

#print(df[['First Name','Position']])
#print(df.iloc[0])
#print(df.loc[8])
#data = {"name":["ali", "sara"], "age":[25, 30]}
#df = pd.DataFrame(data)
#df.index = ['a', 'b']
#print(df.iloc[1])
#print(df.loc['b'])

'''More examples of column selection and accessing rows with iloc and loc'''
#print(df[['Last Name','Salary']])
#print(df.iloc[5])
#print(df.loc[5])

'''Creating DataFrame from dictionary and setting custom index'''
#data = {'name': ['noura', 'hadya', 'shery'], 'age':[32, 27, 29]}
#df = pd.DataFrame(data)
#df.index = ['c', 'd', 'e']
#print(df.iloc[1])
#print(df.loc['d'])


'''Accessing specific cells, slicing rows, and filtering data'''
#print(df.loc[0, 'Salary'])
#print(df.iloc[0:10])
#print(df[df['Salary'] > 70000])

'''Using at and iat to access single cells by label or position'''
#print(df.at[1,'Position'])
#print(df.at[1,'Position'])
#print(df.iat[1,3])

'''Creating DataFrame with custom index and accessing cells with at'''
#df = pd.DataFrame({
#   'A':[1,2,3],
#    'B':[4,5,6]},
#   index = ['x', 'y','z'])
#print(df)
#print(df.at['x','B'])

'''Creating DataFrame and exploring DataFrame properties'''
data = {'name': ['ali', 'mona', 'soad'],
        'age': [25, 30, 22],
        'mark': [88, 67, 70]
        }
df = pd.DataFrame(data)
#print(df)
#print(df.index)
#print(df.columns)
#print(df.values)
#print(df.dtypes)
#print(df.shape)
#print(df.ndim)
#print(df.size)
#print(df.empty)
#print(df.T)
#print(df.axes)