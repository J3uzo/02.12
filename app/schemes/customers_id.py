from pydantic import BaseModel


class SCustomersIdAdd(BaseModel):
    name: str


class SCustomersIdGet(SCustomersIdAdd):
    id: int


class SCustomersIdPatch(BaseModel):
    name: str 