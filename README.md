# final_project

poetry config --local virtualenvs.in-project true poetry init
poetry init -n

.\.venv\Scripts\activate

poetry add fastapi[all]  - add fastapi

uvicorn main:app
uvicorn main:app --port 9200 --reload


ctrl-alt-L 
