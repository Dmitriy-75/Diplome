
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/tasks')
async def tasks_by_user_id (db: Annotated[Session, Depends(get_db)], user_id: int):

    """Хэндлер для получения всех задач по user-id"""
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    return tasks

@router.get('/all_users')
async def all_users(db: Annotated[Session, Depends(get_db)]):

    """Хэндлер для получения всех пользователей"""
    users_all = db.scalars(select(User)).all()
    return users_all


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):

    """Хэндлер для получения  пользователя по id"""
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    return user


@router.post('/create_user')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):

    """Хэндлер для регистрации рользователя"""
    db.execute(insert(User).values(firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   email=create_user.email,
                                   age=create_user.age,
                                   job=create_user.job,
                                  ))
    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'}


@router.put('/update_user')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):

    """Хэндлер для обновления данных пользователя"""
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        email=update_user.email,
        age=update_user.age,
        job=update_user.job))

    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'}


@router.delete('/del_user')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):

    """Хэндлер для удаления пользователя"""
    user_delete = db.scalar(select(User).where(User.id == user_id))
    if user_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(delete(User).where(User.id == user_id))
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User delete is successful!'}


