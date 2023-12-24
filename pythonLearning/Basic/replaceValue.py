import pandas as pd
import numpy as np

# Replace Empty Values

df = pd.DataFrame({'name':['Alfred', pd.NA, 'Catwoman'],
                   'Toy':[np.nan, 'Batmobile', 'Bullwhip'],
                   'Born':[pd.NaT, pd.Timestamp('1940-04-25'),pd.NaT]})

print(df)

df.fillna(130, inplace = True)
print(df)

# Data Cleaning
df_date = pd.DataFrame({"Duration": [60,60,60,45,45,60,60,450,30,60,60],
                   "Pulse": [110,117,103,109,117,102,104,109,98,100,100],
                   "Calories": [409.1,479.0,340.0,282.4,406.0,300.0,374.0,253.3,195.1,269.0,269.0],
                   "Date": ['2020/12/01','2020/12/02','20201203','2020/12/04','2020/12/05',pd.NA,'2020/12/07','2020/12/08','2020/12/09','2020/12/10','2020/12/10']})

print(df_date)
df_date["Date"] = pd.to_datetime(df_date["Date"])
