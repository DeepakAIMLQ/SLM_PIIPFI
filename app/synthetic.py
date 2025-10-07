#Synthetic JSONL generator
#Created By: Deepak Singh 
#Created on: 04-Oct-2025
#Modified On: 07-Oct-2025
#Version: 1.0.0.0
#---------------------------------------------
import json, random
from app.config import FT_DATA_DIR

def generate_synthetic_jsonl(num_samples=200):
    labels_map={"PER":"Name","ORG":"Organization","EMAIL":"Email","PHONE":"Phone",
                "CREDIT":"CreditCard","ACCOUNT":"Account","AMOUNT":"Amount","MED":"MedicalCondition"}
    data=[]
    for _ in range(num_samples):
        text=" ".join([f"Word{i}" for i in range(50)])
        ents=[]
        words=text.split()
        for i, w in enumerate(words):
            if random.random()<0.05:
                label=random.choice(list(labels_map.keys()))
                ents.append({"start":text.find(w),"end":text.find(w)+len(w),"label":labels_map[label]})
        if ents:
            data.append({"text":text,"entities":ents})
    out_file=f"{FT_DATA_DIR}/synthetic_200.jsonl"
    with open(out_file,"w",encoding="utf-8") as fh:
        for item in data: json.dump(item,fh); fh.write("\n")
    return out_file
