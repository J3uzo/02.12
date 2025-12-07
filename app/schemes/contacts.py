from pydantic import BaseModel


class SContactAdd(BaseModel):
    name: str


class SContactGet(SContactAdd):
    id: int


class SContactPatch(BaseModel):
    name: str 