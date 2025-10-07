#PII/PHI/PFI extraction logic
#Created By: Deepak Singh 
#Created on: 04-Oct-2025
#Modified On: 07-Oct-2025
#Version: 1.0.0.0
#---------------------------------------------

from app.chunking import chunk_text
from app.regex_utils import REGEX_PATTERNS, luhn_check
from app.models import ner_general, ner_medical

MED_LEX={"cancer","diabetes","asthma","hypertension","pneumonia","tuberculosis","migraine","covid","malaria"}
TECH_STOP={"sql","server","oracle","python","java","docker","azure","aws","data","project","analytics"}
ORG_SUFFIX=["Ltd","Inc","Corp","LLP","Bank","Company","Technologies","Solutions","Pvt"]

def clean_entity(e): return e.replace("##","").strip(" .,:;()[]-").strip()
def is_heading(t): return t.isupper() and len(t)>2 and len(t.split())<=5
def is_noise(e):
    e=e.strip()
    if len(e)<3: return True
    if is_heading(e): return True
    if e.lower() in TECH_STOP: return True
    return False

def extract_entities(text):
    res={"PII":{"Names":[],"Emails":[],"Phones":[],"Passports":[]},
         "PHI":{"MedicalConditions":[]},
         "PFI":{"Organizations":[],"CreditCards":[],"Accounts":[],"Amounts":[]},
         "ranked_entities":[]}

    # Regex
    for lbl,(pat,wt) in REGEX_PATTERNS.items():
        for m in pat.finditer(text):
            ent=clean_entity(m.group())
            if not ent: continue
            if lbl=="CreditCard" and not luhn_check(ent): continue
            res["ranked_entities"].append({"entity":ent,"label":lbl,"score":wt,"source":"regex"})
            if lbl=="Email": res["PII"]["Emails"].append(ent)
            elif lbl=="Phone": res["PII"]["Phones"].append(ent)
            elif lbl=="CreditCard": res["PFI"]["CreditCards"].append(ent)
            elif lbl=="Account": res["PFI"]["Accounts"].append(ent)
            elif lbl=="Amount": res["PFI"]["Amounts"].append(ent)

    # NER general & medical
    for _,chunk in chunk_text(text):
        try:
            ents = ner_general(chunk[:2000])
            for e in ents:
                ent = clean_entity(e["word"])
                if not ent or is_noise(ent): continue
                label = e["entity_group"]
                score = float(e["score"])
                res["ranked_entities"].append({"entity":ent,"label":label,"score":score,"source":"general"})
                if label in ["PER","PERSON"]: res["PII"]["Names"].append(ent)
                elif label=="ORG" and any(s in ent for s in ORG_SUFFIX): res["PFI"]["Organizations"].append(ent)
        except: pass

        if any(m in chunk.lower() for m in MED_LEX):
            try:
                ents2 = ner_medical(chunk[:2000])
                for e in ents2:
                    ent = clean_entity(e["word"])
                    if any(m in ent.lower() for m in MED_LEX):
                        res["PHI"]["MedicalConditions"].append(ent)
            except: pass

    # Dedup & sort
    for sec in ["PII","PHI","PFI"]:
        for k in res[sec]: res[sec][k]=sorted(set(res[sec][k]))
    res["ranked_entities"].sort(key=lambda x:x["score"],reverse=True)
    return res
