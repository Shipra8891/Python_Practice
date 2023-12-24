# most important package of python
# Pandas data structure - ( series , Data Frame , Panel , Panel 4D )
# Panda Series - very similar to NumPy Array . The only difference is panda series can have index , axis labels
# like when u read a book , at start of book u have content , index . That make it easy to see content
# pandas package needs tp be installed.

import pandas as pd
import numpy as np

my_list = [10, 20, 30]
panda_series = pd.Series(my_list)
print(panda_series)
print(panda_series.index)
print(panda_series.values)  # it converts in to array

# creating series as numPy array

index = ['a', 'b', 'c']
arr = np.array([10, 20, 30])
print(pd.Series(data=arr, index=index))

# creating a series from dictionary

dictionary = {'a': 10, 'b': 20, 'c': 30}
print(pd.Series(dictionary))

# you might be working with JSON , list data which is coming inside python dictionary
# all data which is coming in different format , you want to get all these data in same format
# you can convert then in proper format series and then combine
# data is coming from multiple sources in multiple format - you need to convert these data in single format
# the you can modify these data by transformation ...apply some logc


# using index in series
# main purpose of using Series is understanding its index
# this helps in fatser search or you can say lookup of information

series1 = pd.Series([1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])
series2 = pd.Series([1, 2, 5, 4], index=['USA', 'Germany', 'Italy', 'Japan'])
print(series1)
print(series2)
print(series1 + series2)

# The type int64 tells us that pandas is storing each value
# within this column as a 64 bit integer.
