from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemes.customers import SCustomerGet
    from app.schemes.stages import SStageGet


class SDealAdd(BaseModel):
    name: str
    customer_id: int
    amount: float
    stage_id: int
    probability: str
    date: str
    notes: str 


class SDealGet(SDealAdd):
    id: int


class SDealPatch(BaseModel):
    name: str 
    customer_id: int 
    amount: float 
    stage_id: int 
    probability: str
    date: str 
    notes: str 