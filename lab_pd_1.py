import pandas as pd

#input
file_path = 'transactions.csv'
df = pd.read_csv(file_path, index_col=0)

#main
print(df.loc[df['STATUS'] == 'OK'].sort_values(by = 'SUM', ascending = False)[0:3])

print('===================================')

print('Umbrella, Inc transaction summary: ', df['SUM'][df['CONTRACTOR'] == 'Umbrella, Inc'][df['STATUS'] == 'OK'].sum())

print('\nturtle')