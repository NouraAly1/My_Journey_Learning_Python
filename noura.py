import pandas as pd

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

#print(df[['Last Name','Salary']])
#print(df.iloc[5])
#print(df.loc[5])

#data = {'name': ['noura', 'hadya', 'shery'], 'age':[32, 27, 29]}
#df = pd.DataFrame(data)
#df.index = ['c', 'd', 'e']
#print(df.iloc[1])
#print(df.loc['d'])


#print(df.loc[0, 'Salary'])
#print(df.iloc[0:10])
#print(df[df['Salary'] > 70000])

#print(df.at[1,'Position'])
#print(df.at[1,'Position'])
#print(df.iat[1,3])

#df = pd.DataFrame({
#   'A':[1,2,3],
#    'B':[4,5,6]},
#   index = ['x', 'y','z'])
#print(df)
#print(df.at['x','B'])

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