from PneumoniaDetector import logger
from PneumoniaDetector.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from PneumoniaDetector.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from PneumoniaDetector.pipeline.stage_03_model_training import ModelTrainingPipeline
from PneumoniaDetector.pipeline.stage_04_model_evaluation import EvaluationPipeline
import dagshub
dagshub.init(repo_owner='akhilasurendran002', repo_name='End-to-End-Pneumonia-detection-using-MLflow-and-DVC', mlflow=True)



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


STAGE_NAME = "Model evaluation"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evalution = EvaluationPipeline()
        model_evalution.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
