from fastapi import APIRouter

from app.api.dependencies import DBDep
from app.exceptions.roles import (
    CompaniesAlreadyExistsError,
    CompaniesAlreadyExistsHTTPError,
    CompaniesNotFoundError,
    CompaniesNotFoundHTTPError,
)
from app.schemes.roles import SRoleAdd, SRoleGet
from app.schemes.relations_users_roles import SRoleGetWithRels
from app.services.roles import RoleService

router = APIRouter(prefix="/auth", tags=["Управление ролями"])


@router.post("/roles", summary="Создание новой роли")
async def create_new_role(
    role_data: SRoleAdd,
    db: DBDep,
) -> dict[str, str]:
    try:
        await RoleService(db).create_role(role_data)
    except CompaniesAlreadyExistsError:
        raise CompaniesAlreadyExistsHTTPError
    return {"status": "OK"}


@router.get("/roles", summary="Получение списка ролей")
async def get_all_roles(
    db: DBDep,
) -> list[SRoleGet]:
    return await RoleService(db).get_roles()


@router.get("/roles/{id}", summary="Получение конкретной роли")
async def get_role(
    db: DBDep,
    id: int,
) -> SRoleGetWithRels:
    return await RoleService(db).get_role(role_id=id)


@router.put("/companies/{id}", summary="Изменение конкретной компании")
async def get_role(
    db: DBDep,
    role_data: SRoleAdd,
    id: int,
) -> dict[str, str]:
    try:
        await RoleService(db).edit_role(role_id=id, role_data=role_data)
    except CompaniesAlreadyExistsError:
        raise CompaniesNotFoundHTTPError

    return {"status": "OK"}


@router.delete("/companies/{id}", summary="Удаление конкретной компании")
async def delete_role(
    db: DBDep,
    id: int,
) -> dict[str, str]:
    try:
        await RoleService(db).delete_role(role_id=id)
    except CompaniesNotFoundError:
        raise CompaniesNotFoundHTTPError

    return {"status": "OK"}
