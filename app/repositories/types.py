from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.types import TypeModel
from app.repositories.base import BaseRepository
from app.schemes.types import STypeGet

class TypeRepository(BaseRepository[TypeModel, STypeGet]):
    model = TypeModel
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