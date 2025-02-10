from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel


app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}

@app.get('/users')
def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def id_response(username: str = Path(min_length=5,max_length=20,description='Enter username', example='Eugene'),
        age: int = Path(ge=18,le=120,description='Enter age', example='52')):

    if len(users) != 0:
        new_id = len(users) + 1
    else:
        new_id = 1

    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user



@app.put('/user/{user_id}/{username}/{age}')
async def id_response(username: str = Path(min_length=5,max_length=20,description='Enter username', example='Eugene'),
        age: int = Path(ge=18,le=120,description='Enter age', example='52'), user_id: int = Path(ge=0)):

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    else:
        raise HTTPException(status_code=404, detail='Пользователя не существует')


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, title="User ID", description="Enter User ID", example=1)]) -> User:

    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    else:
        raise HTTPException(status_code=404, detail='Пользователя не существует')
