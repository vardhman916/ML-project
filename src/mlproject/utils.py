import os
import sys #why we importing because we need to handle exception and logging
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database")
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection established with database: %s", mydb)



        df = pd.read_sql_query('select * from call_data',mydb)
        print(df.head())


        return df
    except Exception as ex:
        raise CustomException(ex)