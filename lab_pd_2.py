import pandas as pd
from matplotlib import pyplot as plt

#input
file_path = 'flights.csv'
df = pd.read_csv(file_path, index_col=0)
#main
count = pd.DataFrame({'COUNT': df.groupby(['CARGO']).size()})
summary = df.groupby('CARGO').sum()

data = pd.merge(count, summary, on='CARGO')
print(data)
fig, axis = plt.subplots(1,3)
data['COUNT'].plot(ax=axis[0],xlabel='CARGO', title='Number of flights', kind='bar')
data['PRICE'].plot(ax=axis[2],xlabel='CARGO', title='Total price', kind='bar')
data['WEIGHT'].plot(ax=axis[1],xlabel='CARGO', title='Total weigth', kind='bar')
plt.show()

print('turtle')