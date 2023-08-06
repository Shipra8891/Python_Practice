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
print(df_test1)
print("Shape of dataframe",df_test1.shape)
print("Index of dataframe",df_test1.index)

# rule 1 -copy path and paste here, put r before it.
# rule 2 - change \ to / and print

