from pydantic import BaseModel


class STypeAdd(BaseModel):
    bell: str
    meeting: str
    next_tep: str
    other: str


class STypeGet(STypeAdd):
    id: int


class STypePatch(BaseModel):
    bell: str 
    meeting: str 
    next_tep: str 
    other: str 