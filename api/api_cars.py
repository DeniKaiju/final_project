from fastapi import APIRouter, status
from schemas import NewCarData, SavedCar
from storage import storage

router = APIRouter(
    prefix='/api/cars',
    tags=['API', 'Books'],
)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_car(car: NewCarData) -> SavedCar:
    saved_car = storage.create_car(car.model_dump())
    return saved_car


@router.get('/')
def get_cars() -> list[dict]:
    return [{'mark': 'Volvo', 'engine': '2.0T'}]


@router.put('/update/{car_vin}')
def get_cars() -> list[dict]:
    return [{'mark': 'Volvo', 'engine': '2.0T'}]


@router.delete('/delete/{car_vin}')
def get_cars() -> list[dict]:
    return [{'mark': 'Volvo', 'engine': '2.0T'}]

