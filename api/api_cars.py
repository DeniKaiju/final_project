from fastapi import APIRouter, status
from schemas import NewCarData, SavedCar
from storage import storage

router = APIRouter(
    prefix='/api/cars',
    tags=['API', 'Cars'],
)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_car(car: NewCarData) -> SavedCar:
    saved_car = storage.create_car(car.model_dump())
    return saved_car


@router.get('/')
def get_cars(search_param: str = None, skip: int = 0, limit: int = 10) -> list[SavedCar]:
    cars = storage.get_cars(skip, limit, search_param)
    result = []

    for car in cars:
        instance = SavedCar(**{'mark': car['mark'], 'model': car['model'], 'price': car['price'], 'cover': car['cover'],
                               'tags': car['tags'], 'description': car['description'], 'uuid': car['uuid']})
        result.append(instance)
    return result


@router.patch('/update/{car_id}')
def update_car(car_id: str, price: float = 100.00):
    storage.update_car(car_id, price)
    return {'result': 'OK'}


@router.delete('/delete/{car_vin}')
def delete_car(car_id: str):
    storage.delete_car(car_id)
    return {'deleted': True}
