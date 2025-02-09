from typing import Dict

from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def list():
    return users

@app.get("/")
async def response() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def response() -> str:
    return 'Вы вошли как администратор'

@app.get("/user/{user_id}")
async def response(user_id: int= Path(ge=1,le=100,description='Enter User ID', example='31')) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.post("/user/{username}/{age}")
async def id_response(username: str = Path(min_length=5,max_length=20,description='Enter username', example='Eugene'),
        age: int = Path(ge=18,le=120,description='Enter age', example='52')):
    curr_ind = str(int(max(users, key=int)) + 1)
    users[curr_ind] = {"Имя": username, "возраст": age}
    return f"User {curr_ind} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def id_response(username: str = Path(min_length=5,max_length=20,description='Enter username', example='Eugene'),
        age: int = Path(ge=18,le=120,description='Enter age', example='52'), user_id: int = Path(ge=0)):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"The user {user_id} is updated"}

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id in users:
        users.pop(user_id)
        return {"message": f"Пользователь с ID {user_id} удален."}
    else:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")