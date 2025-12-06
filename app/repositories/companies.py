from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.companies import CompanyModel
from app.repositories.base import BaseRepository
from app.schemes.companies import SCompanyGet

class CompanyRepository(BaseRepository[CompanyModel, SCompanyGet]):
    model = CompanyModel
    schema = SCompanyGet
    
    def get_with_customers(self, company_id: int):
        stmt = select(self.model).where(
            self.model.id == company_id
        ).options(
            selectinload(self.model.customers)
        )
        return self.db.scalar(stmt)
    
    def get_by_name(self, name: str):
        stmt = select(self.model).where(self.model.name.ilike(f"%{name}%"))
        return self.db.scalar(stmt)
    
    def search_companies(self, name: str = None, branch: str = None):
        stmt = select(self.model)
        if name:
            stmt = stmt.where(self.model.name.ilike(f"%{name}%"))
        if branch:
            stmt = stmt.where(self.model.branch.ilike(f"%{branch}%"))
        return self.db.scalars(stmt).all()