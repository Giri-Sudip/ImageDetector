virtaulenv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload