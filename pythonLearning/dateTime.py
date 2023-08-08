from timeit import timeit

import pandas as pd

df_date = pd.DataFrame({'date': ['3/10/2000', '3/11/2000', '3/12/2000'],
                        'values': [2, 3, 4]})
print(df_date)
print(df_date.info())
df_date['date'] = pd.to_datetime(df_date['date'])
print(df_date['date'])
df_date['date'] = pd.to_datetime(df_date['date'], dayfirst=True)
print(df_date['date'])
print(df_date)

print(pd.to_datetime('4/10/2022'))

# The object to convert to a datetime.
# If a DataFrame is provided in the following columns:
# "year", "month", "day".

# custom format
df = pd.DataFrame({'date': ['2016-6-10 20:30:0',
                            '2016-7-1 19:45:30',
                            '2013-10-12 4:5:1'],
                   'value': [2, 3, 4]})
df['date'] = pd.to_datetime(df['date'], format="%Y-%d-%m %H:%M:%S")
print(df['date'])

# infer means assume or predict
# %timeit pd.to_datetime(df['date'], infer_datetime_format=True)
# %timeit pd.to_datetime(df['date'], infer_datetime_format=False)

# handle parsing error
df_error = pd.DataFrame({'date': ['3/10/2000', 'a/11/2000', '3/12/2000'],
                         'value': [2, 3, 4]})
print(df_error)
print("printing date column")
print(df_error['date'])

df_error['date'] = pd.to_datetime(df_error['date'], errors='ignore')
print(df_error)
print(df_error['date'])

df_error['date'] = pd.to_datetime(df_error['date'], errors='coerce')
print(df_error['date'])

# NaT - not at time

# assemble  a datetime from multiple columns

df_assemble = pd.DataFrame({'year': [2015, 2016],
                            'month': [2, 3],
                            'day': [4, 5]})
print(df_assemble)
df_assemble['date'] = pd.to_datetime(df_assemble)

print(df_assemble)

# get year,month and day

df_assemble2 = pd.DataFrame({'name': ['Tom', 'Andy', 'Lucas'],
                             'DoB': ['08-05-1997', '04-28-1996', '12-16-1995']})
print(df_assemble2)
df_assemble2['DoB'] = pd.to_datetime(df_assemble2['DoB'])


df_assemble2['year']= df_assemble2['DoB'].dt.year
df_assemble2['month']= df_assemble2['DoB'].dt.month
df_assemble2['day']= df_assemble2['DoB'].dt.day

print(df_assemble2['year'])
print(df_assemble2['month'])
print(df_assemble2['day'])
print(df_assemble2)

# get the week of year,the day of week and leap year
df_assemble2['week_of_year'] = df_assemble2['DoB'].dt.isocalendar
df_assemble2['day_of_week'] = df_assemble2['DoB'].dt.dayofweek
df_assemble2['is_leap_year'] = df_assemble2['DoB'].dt.is_leap_year

print(df_assemble2['week_of_year'])
print(df_assemble2['day_of_week'])
print(df_assemble2['is_leap_year'])

print(df_assemble2['DoB'].dt.weekday)

dw_mapping={
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
        }
df_assemble2['day_of_week_name'] =df_assemble2['DoB'].dt.weekday.map(dw_mapping)
print(df_assemble2['day_of_week_name'])
print(df_assemble2)

# get the age from the date of birth
today = pd.to_datetime('today')
df_assemble2['age'] = today.year - df_assemble2['DoB'].dt.year
print(df_assemble2['age'])
print(df_assemble2)

