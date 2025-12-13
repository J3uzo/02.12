from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.contacts import ContactModel
from app.repositories.base import BaseRepository
from app.schemes.contacts import SContactGet

class ContactsRepository(BaseRepository[ContactModel, SContactGet]):
    model = ContactModel
    schema = SContactGet
    
    def get_with_reminders(self, contact_id: int):
        stmt = select(self.model).where(
            self.model.id == contact_id
        ).options(
            selectinload(self.model.reminders)
        )
        return self.db.scalar(stmt)
    
    def get_by_name(self, name: str):
        stmt = select(self.model).where(self.model.name.ilike(f"%{name}%"))
        return self.db.scalar(stmt)