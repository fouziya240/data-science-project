import os
import sys

import mysql.connector
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import mysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')



def read_sql_data():
    logging.info("Reading SQL database started")
    try:
          mydb=mysql.connector(
                host=host,
                user=user,
                password=password,
                db=db
          )
          logging.info("connection Established",mydb)
          df=pd.read_sql_query('Select * from student',mydb)
          print(df.head())

          return df


    except Exception as ex:
            raise CustomException(ex)
