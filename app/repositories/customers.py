from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.customers import CustomerModel
from app.repositories.base import BaseRepository
from app.schemes.customers import SCustomerGet
from app.schemes.relations_users_roles import SCustomerGetWithRels

class CustomersRepository(BaseRepository[CustomerModel, SCustomerGet]):
    model = CustomerModel
    schema = SCustomerGet
    
    def get_with_relations(self, customer_id: int) -> SCustomerGetWithRels:
        stmt = select(self.model).where(
            self.model.id == customer_id
        ).options(
            selectinload(self.model.company),
            selectinload(self.model.tag),
            selectinload(self.model.admin),
            selectinload(self.model.deals)
        )
        customer = self.db.scalar(stmt)
        if customer:
            return SCustomerGetWithRels.model_validate(customer)
        return None
    
    def get_by_email(self, email: str):
        stmt = select(self.model).where(self.model.email == email)
        return self.db.scalar(stmt)
    
    def get_by_company_id(self, company_id: int):
        stmt = select(self.model).where(self.model.company_id == company_id)
        return self.db.scalars(stmt).all()
    
    def get_by_tag_id(self, tag_id: int):
        stmt = select(self.model).where(self.model.tag_id == tag_id)
        return self.db.scalars(stmt).all()
    
    def search_customers(self, name: str = None, email: str = None):
        stmt = select(self.model)
        if name:
            stmt = stmt.where(self.model.name.ilike(f"%{name}%"))
        if email:
            stmt = stmt.where(self.model.email.ilike(f"%{email}%"))
        return self.db.scalars(stmt).all()