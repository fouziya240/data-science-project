from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlprojectcomponents.data_ingestion import DataIngestion
from src.mlprojectcomponents.data_ingestion import DataIngestionConfig
from src.mlprojectcomponents.data_transformation import DataTransformation
from src.mlprojectcomponents.data_transformation import DataTransformationConfig  

import sys


if __name__=="__main__":
    logging.info("The execution has started")

try:
    #data_ingestion_config=DataIngestionConfig()
    data_ingestion=DataIngestion
    data_ingestion. __init__ ,data_ingestion()

    #data_transformation_config=DataIngestionConfig()
    data_transformation=DataTransformation
    data_transformation.__init__ ,data_transformation()

except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)