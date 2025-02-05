from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def response() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def response() -> str:
    return 'Вы вошли как администратор'

@app.get("/user/{user_id}")
async def response(user_id: str) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user")
async def id_response(username: str = 'eugene', age: int = 23) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
