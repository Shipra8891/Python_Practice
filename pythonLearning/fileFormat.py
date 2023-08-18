# File Format
# data comes in file
# file can be of different type like pdf, csv, excel, JSON,AVRO.

# JSON - java script object notation

import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

with open("data_file.json", "r") as read_file:
        data = json.load(read_file)

print(data)
print(type(data))

import pandas as pd

jsonStr = '''{"Index0":{"Courses": "Pandas","Discount": "1200"},
           "Index1":{"Courses": "Hadoop","Discount": "1500"},
           "Index2":{"Courses": "Spark","Discount": "1800"}
          }'''

# Convert JSON to DataFrame Using read_json()
df2 = pd.read_json(jsonStr, orient ='index')
print(df2)

print(data['president'])

df3 = pd.DataFrame.from_dict(data, orient ='index')

print(df3)

print("hr data")
hr_df = pd.read_csv('data/hrdata.csv', index_col='Name')

print(hr_df)