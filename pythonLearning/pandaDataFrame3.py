# pivot table - allows to reorganize and summarize selected columns and rows.

import numpy as np
import pandas as pd

from pythonLearning.pandaDataframe import weather_df

data = {
    'A': ['foo','foo','foo','bar','bar','bar'],
    'B': ['one','one','two','two','one','one'],
    'C': ['x','y','x','y','x','y'],
    'D': [1,3,2,5,4,1]
  }
df = pd.DataFrame(data)
print(df)
print("pivot_df")
pivot_df = df.pivot_table(
        values='D',
        index='A',
        columns=['C'],
        aggfunc=np.sum
                         )
print(pivot_df)

print(weather_df[['Temp (C)','Date/Time']])


weather_df['Date/Time'] = pd.to_datetime(weather_df['Date/Time'])
mean_temperature_df = weather_df.pivot_table(
                                              values='Temp (C)',
                                              index=weather_df['Date/Time'].dt.month,
                                              aggfunc=np.mean
                                            )
print(mean_temperature_df)

# group by - this method allows to group rows of data together and
# call aggregate functions to whole the group

#weather_df_group = weather_df.groupby(weather_df['Date/Time'].dt.month).agg(np.mean)['Temp (C)']

#print(weather_df_group)

data = {
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
  'model': ['Citigo', 'Fabia', 'Fiesta', 'Rapid', 'Focus', 'Mondeo', 'Octavia', 'B-Max'],
  'car': ['Skoda', 'Skoda', 'Ford', 'Skoda', 'Ford', 'Ford', 'Skoda', 'Ford']
}

df = pd.DataFrame(data)
print(df)






