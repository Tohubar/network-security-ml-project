import os
import sys
import json
import certifi
import pandas as pd  
import numpy as np  
from dotenv import load_dotenv
from pymongo import MongoClient

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop= True, inplace= True)
            records = list(json.loads(data.T.to_json()).values())
            
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            
            self.mongo_client = MongoClient(DATABASE_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "Network-Security"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path= FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_to_mongodb(records= records, database= DATABASE, collection= Collection)
    print(no_of_records)

 