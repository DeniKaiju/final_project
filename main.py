from fastapi import FastAPI
from api.api_cars import router as api_cars_router

app = FastAPI()
app.include_router(api_cars_router)

@app.get('/')
def root() -> dict:
    return {'try': 'OK', 'count': 10}
