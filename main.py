from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_inegestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_inegestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("Data Initiation Completed")
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate data validation")   
        data_validation_artifact=data_validation.iniatiate_data_validation()
        logging.info("Data Validation Competed")
        print(data_validation_artifact)  
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("Data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config) 
        data_transformation_artifact=data_transformation.initiate_data_tranformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Competed")

        logging.info("Model Trainig Started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transfromation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Mode Training Artifact Created")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
