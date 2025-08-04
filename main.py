from PneumoniaDetector.utils.set_seed import set_global_seed
set_global_seed(42)

from PneumoniaDetector import logger
from PneumoniaDetector.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from PneumoniaDetector.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from PneumoniaDetector.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model "
try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model training"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer= ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
