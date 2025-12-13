from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.stages import StageModel
from app.repositories.base import BaseRepository
from app.schemes.stages import SStageGet

class StagesRepository(BaseRepository[StageModel, SStageGet]):
    model = StageModel
    schema = SStageGet
    
    def get_with_deals(self, stage_id: int):
        stmt = select(self.model).where(
            self.model.id == stage_id
        ).options(
            selectinload(self.model.deals)
        )
        return self.db.scalar(stmt)
    
    def get_by_stage_type(self, stage_type: str):
        stmt = select(self.model).where(
            (self.model.lid == stage_type) | 
            (self.model.success == stage_type) | 
            (self.model.conversation == stage_type) | 
            (self.model.lost == stage_type)
        )
        return self.db.scalar(stmt)