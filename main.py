import pandas as pd
df = pd.read_csv('all_stocks_5yr.csv')

"""data checks"""
print(df.head(2))
print(df.tail(2)) 

"""reading basic data"""
# print(df.columns)
# print(df.Name) #or df.['Name']
# print(df[['Name','date','close']])

"""read a specific location (r,c)"""
# print(df.iloc[2,0])

"""read each row but only include certain columns"""
# for index, row in df.iterrows():
#     print(index,row[['Name','date','open','close']])

"""delete columns that won't be used"""
# df = df.drop('volume', axis=1)

"""or use:"""
df = df.drop(columns=['volume','high', 'low'])
print(df.head(1))

"""rearrange columns"""
df = df[['Name','date','open','close']]
print(df.head(1))

"""find the change in stock price by taking doing close - open"""
df['Net'] = df['close'] - df['open']
print(df.head(1))