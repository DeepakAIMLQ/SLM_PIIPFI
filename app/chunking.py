#Chunking the content Subword wise
#Created By: Deepak Singh 
#Created on: 07-Oct-2025
#Modified On: 07-Oct-2025
#Version: 1.0.0.0
#---------------------------------------------

from app.config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text,size=CHUNK_SIZE,overlap=CHUNK_OVERLAP):
    chunks=[]
    start=0
    while start<len(text):
        end=min(start+size,len(text))
        chunks.append((start,text[start:end]))
        if end==len(text):break
        start +=size-overlap
    return chunks