# DataFrame is primary data structure in panda
# we will learn to find shape and rank of created or existing Dataframe
# how to read dataframe from a file
# learn index in dataframe in panda
# DataFrame are row and column structure
# Dataframe in python comes in Panda library.
# Columns will be of different datatype
# Dataframe has 3 main component - data, index column
# Dataframe() function will be used to create datafareme

import pandas as pd
import csv
import numpy as np

pd.set_option('display.max_columns',10)
pd.set_option('display.width',900)

df1 = pd.DataFrame([[1, 2, 3],
                    [3, 4, 5],
                    [5, 6, 7],
                    [7, 8, 9]])
print(df1)
print(type(df1))
print("Shape:", df1.shape)
# Shape-no. of rows and column
print("Index:", df1.index)

# Indexing
df2 = pd.DataFrame([[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
                   , index=['a', 'b', 'c', 'd']
                   , columns=['x', 'y', 'z']
                   )
print("Shape:", df2.shape)
print("index:", df2.index)
print(df2)

# reading data frame from file
df_test1 = pd.read_csv(r"/pythonLearning/a.csv")

# rule 1 -copy path and paste here, put r before it.
# rule 2 - change \ to / and print


print(df_test1)
print("Shape of dataframe", df_test1.shape)
print("Index of dataframe", df_test1.index)

print(df_test1.head(2))
print(df_test1.head(3))
print(df_test1['name'].head(3))

print("------- dataframe analyze-------")
# .info() - it is a fuction which give information

print(df_test1.info())

# .head() - it gives total rows data.
# by default, it gives 5 rows data only....head()
# if you want more data write under head bracket
# head print from top
# tail print last or from bottom

print(df_test1.tail(2))

# .index -
print(df_test1.index)

# .unique() - select unique column values

print(df_test1['city'].unique())
# .nunique() - number of unique value.
# It will not consider null values or blank values


print(df_test1['city'].nunique())

# value_counts

print(df_test1['city'].value_counts())

print("______________________________Data Manupulation________________________")
# first we create data frame by using csv file or manually.
# now based on the requirement we transform and modify, manipulate the above created dataframe.

# creating weather data frame
weather_df = pd.read_csv(r"/pythonLearning/weather_2012.csv")
print(weather_df)
print(weather_df.head(5))
print(weather_df.info())

print(weather_df['Weather'].head())
print(weather_df[['Weather','Temp (C)']].head())

# whenever need to take more than two columns need to put double square bracket.
# for getting the first n rows from a dataframe we can use .head(n) or [:n]

print(weather_df.head(3))
print(weather_df[:3])
print(weather_df[0:6:2])
print(weather_df[0:10:2]['Date/Time'])

print(weather_df[0:10:2][['Date/Time','Wind Spd (km/h)']])

# using slicing we can display either whole rows or any particular column as per the user requirment.

# .loc (for label location) and .iloc (for integer location)
# .loc goes on the label basis and .iloc goes on the index basis

print(weather_df.loc[0:5,['Visibility (km)','Rel Hum (%)']])
print(weather_df.iloc[0:5][['Visibility (km)','Rel Hum (%)']])

# filtering
# take input data -- filter --output data
# by filtering rows in dataframe give specific rows from entire dataset.

print(weather_df['Weather'].unique())
snowed_filter = weather_df['Weather'].str.lower().str.contains('snow')
print(snowed_filter)
# this will give boollen output (True or False) Masking
print(weather_df['Weather'].iloc[8779])
print(weather_df['Weather'].iloc[4])
print(weather_df[snowed_filter])

# filtering on exiting dataframe based on conditions
# to create a new transformed dataframe
# pd.set_option('display.max_columns',n) - in this we write the number of columns required
# pd.set_option('display.width',n) - in this we write the width


transform_dataframe = weather_df[(weather_df['Wind Spd (km/h)'] > 24)
                                 & (weather_df['Visibility (km)']== 25)
                                  ]

print("Transformed Dataframe Result")
print(transform_dataframe.head())

# modify only one column as per user requirment
add_10 = weather_df["Wind Spd (km/h)"] + 10
print(add_10.head())
print(add_10.head(10))