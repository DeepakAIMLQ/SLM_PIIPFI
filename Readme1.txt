-- Run Dependencies
>> pip install -r requirements.txt

-- Run FrontEnd 
>> streamlit run test_client.py
or for docker in same as fronend
>> streamlit run test_client.py --server.port 8501 --server.address 0.0.0.0
use url http://localhost:8501/

-- Run Backend

>> uvicorn app.main:app --reload
or for docker in same as streamlit
>> uvicorn app.main:app --host 0.0.0.0 --port 8000 &  
use url http://localhost:8000/docs
