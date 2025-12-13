from app.database.database import async_session_maker
from app.repositories.roles import RolesRepository
from app.repositories.users import UsersRepository
from app.repositories.customers import CustomersRepository
from app.repositories.companies import CompaniesRepository
from app.repositories.contacts import ContactsRepository
from app.repositories.deals import DealsRepository
from app.repositories.stages import StagesRepository
from app.repositories.tags import TagsRepository
from app.repositories.types import TypesRepository
from app.repositories.reminders import RemindersRepository


class DBManager:
    def __init__(self, session_factory: async_session_maker):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        # TODO Добавить сюда созданные репозитории
        # Пример:
        self.users = UsersRepository(self.session)
        self.roles = RolesRepository(self.session)
        self.customers = CustomersRepository(self.session)
        self.companies = CompaniesRepository(self.session)
        self.contacrs = ContactsRepository (self.session)
        self.deals = DealsRepository (self.session)
        self.stages = StagesRepository (self.session)
        self.tags = TagsRepository (self.session)
        self.types = TypesRepository (self.session)
        self.reminders = RemindersRepository (self.session)
        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
