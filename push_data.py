
import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("Mongo_Db_url")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import pymongo  
import numpy as np
from pymongo import MongoClient
from networksecurity.exception import exception
from networksecurity.logging import logger

class NetworkDataExtract():
    def __init__(self):
       try:
           pass
       except Exception as e:
           raise exception(e)
    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise exception(e)
    
    def push_data_to_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection  
            self.records=records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise exception(e,sys)


if __name__=="__main__":
    try:
        FILE_PATH="Network_Data\phisingData.csv"
        DATABASE="NetworkSecurity"
        COLLECTION="PhisingData"
        obj=NetworkDataExtract()
        records=obj.cv_to_json_convertor(FILE_PATH)
        no_of_records=obj.push_data_to_mongodb(obj.cv_to_json_convertor(FILE_PATH),DATABASE,COLLECTION)
        print(f"Number of records inserted in the collection {COLLECTION} is {no_of_records}")
    except Exception as e:
        raise exception(e,sys)
