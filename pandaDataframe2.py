# working with columns - modification of dataframe.
# like - add or update columns, rename columns, delete or drop columns
# modification by using (+,*,/) operator.


# from pythonLearning.pandaDataframe import weather_df
from pythonLearning.pandaDataframe import *
import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 900)

print(weather_df.head())
print(weather_df["Visibility (km)"].head())

add_2 = weather_df["Visibility (km)"] + 2
print(add_2.head())

mult_2 = weather_df["Visibility (km)"] * 2 + 2
print(mult_2.head())

div_2 = weather_df["Visibility (km)"] / 2
print(div_2.head())

# add two columns
print(weather_df["Temp (C)"])
print(weather_df["Dew Point Temp (C)"])
print((weather_df["Temp (C)"] + weather_df["Dew Point Temp (C)"]).head(3))
weather_df['new_temp_col'] = weather_df["Temp (C)"] + weather_df["Dew Point Temp (C)"].head(3)
print(weather_df['new_temp_col'].head(3))


# .apply() - if u want to do any operation on large scale or in bulk on any particular column

def times2(value):
    return value * 2


print(weather_df["Visibility (km)"].head())
print(weather_df["Visibility (km)"].apply(times2).head())

# .describe()
print(weather_df["Visibility (km)"].describe())

# .rename()
print(weather_df.rename(columns={"Visibility (km)": "Visibility (kilometer)"}, inplace=True))
print("current status of weather_df")
print(weather_df.head())

# .drop()
drop_df = weather_df.drop(labels=['Wind Spd (km/h)'], axis=1).head(3)
print("Dropped Wind Spd (km/h) ")
print(drop_df)

#.sort_values()
sorted_by_temp = weather_df.sort_values('Temp (C)',ascending=True)
print(".sort_values")
print(sorted_by_temp.head())

#

