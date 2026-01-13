import pandas as pd

#df = pd.read_excel('employee.xlsx')
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

#data = {'name': ['ali', 'mona', 'soad'],
#        'age': [25, 30, 22],
#        'mark': [88, 67, 70]
#       }
#df = pd.DataFrame(data)
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
#print(df.isna())
#print(df.notna())
#print(df.describe())
#print(df.info())
#print(df.head(2))
#print(df.tail(2))

employee = pd.read_excel("Employee.xlsx")
print(employee)
print("*" * 20)
#print(type(employee['First Name']))
#print(type(employee[['First Name']]))
#print(employee[['First Name', 'Salary']])
#print(employee.isnull())
#print(employee.isnull().sum())

#df = employee.dropna()
#print(df)
#employee.dropna(how='all')
#employee.dropna(subset='First Name')

# fill empty cells
#df = employee.fillna(value='Not Found')
#print(df)

#df = employee.fillna({'Salary':0, 'Position':'Not Hired'})
#print(df)

#df = employee.sort_values(by='First Name' , ascending= False)
#print(df)

#df = employee.sort_values(by='Salary')
#print(df)

# search with conditions
#print(employee[employee['Position'] == "Data Analyst"])
#print(employee[(employee['Position'] == "Data Analyst") & (employee['Salary'] > 10000)])

#copy_employee = employee.copy()
#print(copy_employee)

#view_employee = employee['Salary']
#print(view_employee)

# ste - contains melt pivot pivot_table stack unstack

#df = pd.DataFrame({'gmail':['ali@gmail.com', 'mona', 'sara', 'sama', 'mohamed']})
#print(df)
#df['upper_names'] = df['Name'].str.lower()
#print(df)
#df['is_gmail'] = df['gmail'].str.contains('@gmail.com')
#print(df)

df = pd.DataFrame({'student': ['A','B'],
                   'math': [90, 95],
                   'science':[85, 99]
                   })
print(df)

df_melted = pd.melt(df,
                    id_vars= 'student',
                    value_vars=['math', 'science'],
                    var_name= 'subject',
                    value_name= 'marks',
                    ignore_index= False
)
print(df_melted)

df_pivot = df_melted.pivot(index = 'student', columns = 'subject', values = 'marks')
print(df_pivot)