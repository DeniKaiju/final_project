from fastapi import FastAPI
from api import api_cars
from web import web_cars

app = FastAPI()
app.include_router(api_cars.router)
app.include_router(web_cars.router)


@app.get('/')
def root() -> dict:
    return {'try': 'OK', 'count': 10}
