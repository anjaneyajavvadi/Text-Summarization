from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
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