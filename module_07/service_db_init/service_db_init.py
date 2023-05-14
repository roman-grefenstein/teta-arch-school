from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://admin:admin@db-node-ex01/archdb?retryWrites=true&w=majority", authSource="admin")  # Remember your uri string
col = client.college["authors"]

col.drop()

# добавление по одному
df = pd.read_json("ExportJson.json",orient='records')

all_data = []
for index, row in df.iterrows():
    row['_id'] = str(index+1)    
    all_data.append(row.to_dict())    

col.insert_many(all_data)
