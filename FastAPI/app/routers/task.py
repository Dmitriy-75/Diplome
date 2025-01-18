
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db

from typing import Annotated
from app.models.task import Task
from app.models.user import User
from app.schemas import CreateTask, UpdateTask

from sqlalchemy import insert, select, update, delete
from slugify import slugify
from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/task",tags=["task"])
DbSession = Annotated[Session, Depends(get_db)]

@router.get("/")
async def all_tasks(db: DbSession):

    '''Хендлер для получения всех задач'''
    all_tasks = db.scalars(select(Task)).all()
    return all_tasks


@router.get('/task')
async def task_by_id(task_id:int, db: DbSession):
    '''Хендлер для получения задачи по id'''
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found")
    return task


@router.post("/create")
async def create_task(db: DbSession, cr_task: CreateTask, user_id: int):

    '''Хендлер для создания задачи'''
    check_id = db.scalars(select(User).where(User.id == user_id))
    if check_id is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found")

    db.execute(insert(Task).values(title=cr_task.title,
                                   content=cr_task.content,
                                   priority=cr_task.priority,
                                   completed= cr_task.completed,
                                   user_id=user_id,
                                   slug=slugify(cr_task.title)
                                   ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update")
async def update_task(db: DbSession, task_id:int, upd_task: UpdateTask):

    '''Хендлер для обновления задачи'''
    check_id = db.scalar(select(Task).where(Task.id == task_id))
    if check_id is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found")

    db.execute(update(Task).where(Task.id == task_id).values(
                                title=upd_task.title,
                                content=upd_task.content,
                                priority=upd_task.priority,
                                completed=upd_task.priority,
                                user_id=upd_task.user_id,
                                ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successfull'}


@router.delete("/delete")
async def delete_task(db: DbSession, task_id:int):

    '''Хендлер для удаления задачи'''
    check_id = db.scalars(select(Task).where(Task.id == task_id))
    if check_id is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}