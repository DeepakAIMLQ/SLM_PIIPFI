#NER Pipeline Loader
#Created By: Deepak Singh 
#Created on: 07-Oct-2025
#Modified On: 07-Oct-2025
#Version: 1.0.0.0
#---------------------------------------------

from transformers import pipeline
from app.config import NER_MODEL_GENERAL, NER_MODEL_MEDICAL, DEVICE

ner_general = pipeline("ner", model=NER_MODEL_GENERAL, aggregation_strategy="simple", device=DEVICE)
ner_medical = pipeline("ner", model=NER_MODEL_MEDICAL, aggregation_strategy="simple", device=DEVICE)
