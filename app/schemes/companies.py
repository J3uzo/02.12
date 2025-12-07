from pydantic import BaseModel


class SCompanyAdd(BaseModel):
    name: str
    branch: str 
    number: str 
    email: str 
    address: str 
    web: str 


class SCompanyGet(SCompanyAdd):
    id: int


class SCompanyPatch(BaseModel):
    name: str 
    branch: str 
    number: str 
    email: str 
    address: str 
    web: str 