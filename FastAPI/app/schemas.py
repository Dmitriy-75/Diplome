from pydantic import BaseModel, EmailStr, Field


class CreateUser (BaseModel):

    firstname: str = Field(min_length=2)
    lastname: str = Field(min_length=2)
    email: EmailStr
    age: int = Field(gt=16,lt=99)
    job: str = Field(min_length=2)



class UpdateUser (BaseModel):
    firstname: str = Field(min_length=2)
    lastname: str = Field(min_length=2)
    email: EmailStr
    age: int = Field(gt=16,lt=99)
    job: str = Field(min_length=2)


class CreateTask (BaseModel):
    title: str
    content: str
    priority: int = Field(gt=0)
    completed: bool = Field(default=False)

class UpdateTask (BaseModel):
    title: str
    content: str
    priority: int = Field(gt=0)
    completed: bool = Field(default=False)
    user_id: int = Field(gt=0)


    class Config:
        orm_mode = True

