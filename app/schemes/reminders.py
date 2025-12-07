from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemes.types import STypeGet
    from app.schemes.contacts import SContactGet


class SReminderAdd(BaseModel):
    name: str
    description: str | None = None
    date: str
    type_id: int | None = None
    contact_id: int | None = None


class SReminderGet(SReminderAdd):
    id: int


class SReminderPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    date: str | None = None
    type_id: int | None = None
    contact_id: int | None = None