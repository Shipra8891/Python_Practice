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
df_test1 = pd.read_csv(r"C:\Users\Shipra\PycharmProjects\PythonPractice\pythonLearning\a.csv")

# rule 1 -copy path and paste here, put r before it.
# rule 2 - change \ to / and print


print(df_test1)
print("Shape of dataframe",df_test1.shape)
print("Index of dataframe",df_test1.index)

print(df_test1.head(2))
print(df_test1.head(3))
print(df_test1['name'].head(3))

print("------- dataframe analyze-------")
# .info() - it is a fuction which give information

print(df_test1.info())

# .head() - it gives total rows data.
# by default it gives 5 rows data only....head()
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

#value_counts

print(df_test1['city'].value_counts())

print("______________________________Data Manupulation________________________")
# first we create data frame by using csv file or manually.
# now based on the requirement we transform and modify, manupulate the above created dataframe.

# creating weather data frame
weather_df = pd.read_csv(r"C:\Users\Shipra\PycharmProjects\PythonPractice\pythonLearning\weather_2012.csv")
print(weather_df)
print(weather_df.head(5))

