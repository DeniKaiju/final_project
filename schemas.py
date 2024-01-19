from pydantic import BaseModel, Field
from constants import Marks


class NewCarData(BaseModel):
    mark: str = Field(min_length=3, examples=['Audi'])
    model: str = Field(min_length=2, examples=['A4'])
    price: float = Field(default=0.01, gt=0.0)
    cover: str
    tags: list[Marks] = Field(default=[], max_items=1) #todo
    description: str = None


class SavedCar(NewCarData):
    uuid: str = Field(examples=['28a118b0-0e13-4395-9293-f954a411bc0f'])
