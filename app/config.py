#Configuration and Constants
#Created By: Deepak Singh 
#Created on: 07-Oct-2025
#Modified On: 07-Oct-2025
#Version: 1.0.0.0
#---------------------------------------------
import os
from pathlib import Path
import torch

INPUT_DIR="input"
OUTPUT_DIR="output"
FT_DATA_DIR="ft_data"
os.makedirs(OUTPUT_DIR,exist_ok=True)
os.makedirs(FT_DATA_DIR,exist_ok=True)

NER_MODEL_GENERAL = "dslim/bert-base-NER"
NER_MODEL_MEDICAL = "d4data/biomedical-ner-all"
DEVICE = 0 if torch.cuda.is_available() else -1

CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200
HF_TRUNCATE = 2000