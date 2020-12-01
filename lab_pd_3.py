import pandas as pd
from matplotlib import pyplot as plt

#input
file_path1 = 'students_info.xlsx'
file_path2 = 'results_ejudge.html'
df1 = pd.read_excel(file_path1, index_col=0)
df2 = pd.read_html(file_path2, index_col=0)[0]
df = pd.merge(df1,df2, left_on='login', right_on='User')

#main?
groupbyFaculty = df.groupby(by='group_faculty').mean()
groupbyOut = df.groupby(by='group_out').mean()

#Task 1 output
fig, axis = plt.subplots(1,2)
groupbyFaculty['Solved'].plot(ax=axis[0], xlabel='group_faculty', kind='bar')
groupbyOut['Solved'].plot(ax=axis[1],xlabel='group_out', kind='bar')
plt.setp(axis, ylim=(0,8))
#plt.show()

#Task 2 output
#print(df[(df['G'] > 10) | (df['H'] > 10)]) #to see the genius dataFrame
print('From faculties:', pd.unique(df[(df['G'] > 10) | (df['H'] > 10)]['group_faculty']))
print('to groups:', pd.unique(df[(df['G'] > 10) | (df['H'] > 10)]['group_out']))

'''#dlc to Task 2, not an additional task
print()
for i in range(len(df[(df['G'] > 10) | (df['H'] > 10)].index)):
    print('student', df[(df['G'] > 10) | (df['H'] > 10)].iat[i,2],
          'from faculty', df[(df['G'] > 10) | (df['H'] > 10)].iat[i,0],
          'to group', df[(df['G'] > 10) | (df['H'] > 10)].iat[i,1])'''

print('\nturtle')