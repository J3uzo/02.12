from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.tags import TagModel
from app.repositories.base import BaseRepository
from app.schemes.tags import STagGet

class TagsRepository(BaseRepository[TagModel, STagGet]):
    model = TagModel
    schema = STagGet
    
    def get_with_customers(self, tag_id: int):
        stmt = select(self.model).where(
            self.model.id == tag_id
        ).options(
            selectinload(self.model.customers)
        )
        return self.db.scalar(stmt)
    
    def get_by_tag_type(self, tag_type: str):
        stmt = select(self.model).where(
            (self.model.VIP == tag_type) | 
            (self.model.activ == tag_type) | 
            (self.model.partner == tag_type)
        )
        return self.db.scalar(stmt)