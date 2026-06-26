from pymongo.mongo_client import MongoClient
import  pandas as pd
import json

uri= "mongodb+srv://trisha:12345@cluster0.oxvtvnl.mongodb.net/?appName=Cluster0"

client= MongoClient(uri)

DATABASE_NAME= "wafer_fault"
COLLECTION_NAME= "sensor_fault_detection"

df=pd.read_csv("C:\Users\dastr\Downloads\Sensor Project\Notebooks\wafer_23012020_041211.csv")

df=df.drop('Unnamed: 0',axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

