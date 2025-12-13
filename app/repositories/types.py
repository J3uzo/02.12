from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.types import RemindTypeModel
from app.repositories.base import BaseRepository
from app.schemes.types import STypeGet

class TypesRepository(BaseRepository[RemindTypeModel, STypeGet]):
    model = RemindTypeModel
    schema = STypeGet
    
    def get_with_reminders(self, type_id: int):
        stmt = select(self.model).where(
            self.model.id == type_id
        ).options(
            selectinload(self.model.reminders)
        )
        return self.db.scalar(stmt)
    
    def get_by_type_name(self, type_name: str):
        stmt = select(self.model).where(
            (self.model.bell == type_name) | 
            (self.model.meeting == type_name) | 
            (self.model.next_step == type_name) | 
            (self.model.other == type_name)
        )
        return self.db.scalar(stmt)