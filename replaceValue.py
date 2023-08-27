import pandas as pd
import numpy as np

# Replace Empty Values

df = pd.DataFrame({'name':['Alfred', pd.NA, 'Catwoman'],
                   'Toy':[np.nan, 'Batmobile', 'Bullwhip'],
                   'Born':[pd.NaT, pd.Timestamp('1940-04-25'),pd.NaT]})

print(df)

df.fillna(130, inplace = True)
print(df)