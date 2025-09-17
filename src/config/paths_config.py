import os
from pathlib import Path
########################### DATA INGESTION #########################

RAW_DIR = "artifacts/raw"
RAW_FILE_PATH = Path(RAW_DIR,"raw.csv")
TRAIN_FILE_PATH = Path(RAW_DIR,"train.csv")
TEST_FILE_PATH = Path(RAW_DIR,"test.csv")

CONFIG_PATH = "src/config/config.yaml"


######################## DATA PROCESSING ########################

PROCESSED_DIR = "artifacts/processed"
PROCESSED_TRAIN_DATA_PATH = Path(PROCESSED_DIR,"processed_train.csv")
PROCESSED_TEST_DATA_PATH = Path(PROCESSED_DIR,"processed_test.csv")


####################### MODEL TRAINING #################
MODEL_OUTPUT_PATH = "artifacts/models/lgbm_model.pkl"