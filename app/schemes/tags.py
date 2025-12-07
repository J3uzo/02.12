from pydantic import BaseModel


class STagAdd(BaseModel):
    VIP: str
    activ: str
    partner: str


class STagGet(STagAdd):
    id: int


class STagPatch(BaseModel):
    VIP: str | None = None
    activ: str | None = None
    partner: str | None = None