import pandas as pd
import plotly_express as px
import pandas_datareader as fin
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
# df = df.drop(columns=['volume','high', 'low'])

"""rearrange columns"""
df = df[['Name','date','open','close']]

"""find the change in stock price by taking doing close - open"""
df['net'] = df['close'] - df['open']
print(df.head(1))

"""create new csv"""
df.to_csv('s&p500 cleaned',index=False)

#----step2----#

"""plot the data"""
figure = px.line(title='Stock Chart')
figure.add_scatter(x=df.index, y=df['net'], mode='lines')
figure.show()