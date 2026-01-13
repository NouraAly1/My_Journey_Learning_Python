import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Employee.xlsx')
print(df)
print(('*')* 30)

#plt.figure(figsize=(5,12))
#plt.plot(df['First Name'], df['Salary'])
#plt.title('employee salaries by first name')
#plt.xlabel('first name')
#plt.ylabel('salary')
#plt.xticks(rotation = 45)
#plt.tight_layout()
#plt.show()

#if i want bar chart:
#plt.bar(df['First Name'], df['Salary'])
#if i want a scatter shape:
#plt.scatter(df['First Name'], df['Salary'])

#if i want pie chart with percentage:
#position_counts = df['Position'].value_counts()
#plt.pie(position_counts, labels=position_counts.index, autopct='%1.1f%%')
#plt.title('pie chart - position distribution')
#plt.show()






#df = pd.DataFrame({
#    'student':['ahmed', 'mohamed', 'ali', 'nour', 'wael'],
#    'math': [85, 90, 78, 92, 88],
#    'science': [80, 85, 82, 89, 84],
#    'english': [78, 75, 80, 85, 90]
#})

#df.plot(kind='bar', x='student', y='math', title='math score diagram', color='orange')
#plt.ylabel('mathscore')
#plt.grid(False)
#plt.tight_layout()
#plt.show()

#df.plot(kind='bins', bins=5, color= 'orange', title= 'subject score diagram')
#plt.xlabel('score')
#plt.ylabel('mse')
#plt.show()

#df[['math', 'science']].plot(kind='box', title='math and science diagram', )
#plt.xlabel('subject')
#plt.ylabel('score')
#plt.show()

#df.set_index('student').plot(kind='area', alpha=1, title='area diagram ')
#plt.show()
# if not for all of subjects
#df.set_index('student')[['math', 'science']].plot(kind='area', alpha=1)
#plt.ylabel('score')
#plt.show()    

#df.set_index('student').plot(subplots=True, layout=[3,1], figsize=(6,8), title='subplot')
#plt.show()

#ME = df.plot(kind='line',
#             x='student',
#             y='math',
#             color='blue',
#             title='math score'
#             )
#df.plot(kind='line',
#        x='student',
#        y='english',
#        color='red',
#        secondary_y= True,
#        ax=ME,
#        title='english score'
#         )
#plt.show()

