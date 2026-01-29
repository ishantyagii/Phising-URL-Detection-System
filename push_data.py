import os, sys, json
from dotenv import load_dotenv
from dotenv import dotenv_values
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# ---- load .env from the same folder as this script ----
ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")
print("Loading .env from:", ENV_PATH)
load_dotenv(dotenv_path=ENV_PATH, override=True)
parsed = dotenv_values(ENV_PATH)
print("Parsed .env keys/values ->", parsed)
print("Parsed .env keys/values ->", dotenv_values())

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("Mongo host ->", (MONGO_DB_URL or "MISSING").split('@')[-1].split('/')[0] if MONGO_DB_URL else "MISSING")
if not MONGO_DB_URL:
    raise RuntimeError("MONGO_DB_URL is missing. Put it in your .env next to push_data.py")

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            # (Your original method kept) — works fine
            records = list(json.loads(df.T.to_json()).values())
            return records
            # Alternatively: records = df.to_dict(orient="records")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            # IMPORTANT: pass certifi for Atlas TLS
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=certifi.where(),
                serverSelectionTimeoutMS=20000
            )
            self.database   = self.mongo_client[database]    # Database object
            self.collection = self.database[collection]      # Collection object
            result = self.collection.insert_many(records)
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE  = "ISHANAI"
    Collection = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records[:2])  # preview
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)

        


