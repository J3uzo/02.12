from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload

from app.models.reminders import ReminderModel
from app.repositories.base import BaseRepository
from app.schemes.reminders import SReminderGet
from app.schemes.relations import SReminderGetWithRels

class ReminderRepository(BaseRepository[ReminderModel, SReminderGet]):
    model = ReminderModel
    schema = SReminderGet
    
    def get_with_relations(self, reminder_id: int) -> SReminderGetWithRels:
        stmt = select(self.model).where(
            self.model.id == reminder_id
        ).options(
            selectinload(self.model.type),
            selectinload(self.model.contact),
            selectinload(self.model.admin)
        )
        reminder = self.db.scalar(stmt)
        if reminder:
            return SReminderGetWithRels.model_validate(reminder)
        return None
    
    def get_by_type_id(self, type_id: int):
        stmt = select(self.model).where(self.model.type_id == type_id)
        return self.db.scalars(stmt).all()
    
    def get_by_contact_id(self, contact_id: int):
        stmt = select(self.model).where(self.model.contact_id == contact_id)
        return self.db.scalars(stmt).all()
    
    def get_by_date_range(self, start_date: str, end_date: str):
        stmt = select(self.model).where(
            and_(
                self.model.date >= start_date,
                self.model.date <= end_date
            )
        ).order_by(self.model.date)
        return self.db.scalars(stmt).all()
    
    def get_upcoming_reminders(self, from_date: str, to_date: str):
        return self.get_by_date_range(from_date, to_date)