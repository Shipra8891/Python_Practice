import pandas as pd
df_dateIndex1 = pd.read_csv(r"/pythonLearning/data/city_sales.csv")
print("Original New Dataframe")
print(df_dateIndex1.head())
df_dateIndex1.info()

# improve performance by setting date column as the index

df_dateIndex2 = pd.read_csv('../data/city_sales.csv', parse_dates=['date'])
print("Second dataframe Information")
df_dateIndex2.info()

print("new dataframe data details")
print(df_dateIndex2)

df_dateIndex3 = df_dateIndex2.set_index(['date'])
print("New Dataframe with .set_index")
print(df_dateIndex3)

print("select data with specific year and perform aggregation")
print(df_dateIndex3.loc['2018'])

print("SUM data with specific year and perform aggregation")

print(df_dateIndex3.loc['2018','num'].sum())

print("Group By data with specific year and perform aggregation")

print(df_dateIndex3.loc['2018'].groupby('city').sum())

# select data with specific month or a specific day of the month
print("selecting 5 month of 2018")
df_dateIndex4 = df_dateIndex3.loc['2018-5']
print(df_dateIndex4)

print("selecting 1/5/2018")
df_dateIndex4 = df_dateIndex3.loc['2018-5-1']
print(df_dateIndex4)

# select data between two dates

df_dateIndex4 = df_dateIndex3.loc['2016':'2018']
print(df_dateIndex4)

df_dateIndex4 = df_dateIndex3.loc['2018-5-2':'2018-5-11']
print(df_dateIndex4)

df_dateIndex4 = df_dateIndex3.loc['2018-5-2 10:30':'2018-5-11 10:45']
print(df_dateIndex4)

df_dateIndex4= df_dateIndex3.between_time('10:30','10:45')
print(df_dateIndex4)

df_null = pd.read_csv(r"/pythonLearning/a.csv")
print("-----------meaning of fillna --------------")
print(df_null)
newdf = df_null.fillna(222222)
print("-----------meaning of fillna --------------")
print(newdf)
