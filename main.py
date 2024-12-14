from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME="DATA INGESTION STAGE"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info(f"stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="DATA VALIDATION STAGE"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation_training_pipeline = DataValidationTrainingPipeline()
    data_validation_training_pipeline.main()
    logger.info(f"stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="DATA TRANSFORMATION STAGE"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation_training_pipeline = DataTransformationTrainingPipeline()
    data_transformation_training_pipeline.main()
    logger.info(f"stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    model_training_pipeline= ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f"stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e