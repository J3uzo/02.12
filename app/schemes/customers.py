from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemes.companies import SCompanyGet
    from app.schemes.tags import STagGet


class SCustomerAdd(BaseModel):
    name: str
    email: str 
    number: str 
    company_id: int 
    post: str 
    tag_id: int 


class SCustomerGet(SCustomerAdd):
    id: int


class SCustomerPatch(BaseModel):
    name: str 
    email: str 
    number: str 
    company_id: int 
    post: str 
    tag_id: int