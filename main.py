import pandas as pd
df = pd.read_csv('all_stocks_5yr.csv')

"""data checks"""
# print(df.head(2))
# print(df.tail(2)) 

"""reading basic data"""

# print(df.columns)
# print(df.Name) #or df.['Name']
# print(df[['Name','date','close']])

"""read a specific location (r,c)"""
# print(df.iloc[2,0])

"""read each row"""
for index, row in df.iterrows():
    print(index,row[['Name','date','open','close']])

