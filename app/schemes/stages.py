from pydantic import BaseModel


class SStageAdd(BaseModel):
    lid: str
    success: str
    conversation: str
    lost: str


class SStageGet(SStageAdd):
    id: int


class SStagePatch(BaseModel):
    lid: str | None = None
    success: str | None = None
    conversation: str | None = None
    lost: str | None = None