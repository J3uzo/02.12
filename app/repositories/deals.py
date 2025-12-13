from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload

from app.models.deals import DealModel
from app.repositories.base import BaseRepository
from app.schemes.deals import SDealGet
from app.schemes.relations_users_roles import SDealGetWithRels

class DealsRepository(BaseRepository[DealModel, SDealGet]):
    model = DealModel
    schema = SDealGet
    
    def get_with_relations(self, deal_id: int) -> SDealGetWithRels:
        stmt = select(self.model).where(
            self.model.id == deal_id
        ).options(
            selectinload(self.model.customer),
            selectinload(self.model.stage),
            selectinload(self.model.admin)
        )
        deal = self.db.scalar(stmt)
        if deal:
            return SDealGetWithRels.model_validate(deal)
        return None
    
    def get_by_customer_id(self, customer_id: int):
        stmt = select(self.model).where(self.model.customer_id == customer_id)
        return self.db.scalars(stmt).all()
    
    def get_by_stage_id(self, stage_id: int):
        stmt = select(self.model).where(self.model.stage_id == stage_id)
        return self.db.scalars(stmt).all()
    
    def get_by_amount_range(self, min_amount: float, max_amount: float):
        stmt = select(self.model).where(
            and_(
                self.model.amount >= min_amount,
                self.model.amount <= max_amount
            )
        )
        return self.db.scalars(stmt).all()
    
    def get_by_date_range(self, start_date: str, end_date: str):
        stmt = select(self.model).where(
            and_(
                self.model.date >= start_date,
                self.model.date <= end_date
            )
        )
        return self.db.scalars(stmt).all()