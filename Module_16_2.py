from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def response() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def response() -> str:
    return 'Вы вошли как администратор'

@app.get("/user/{user_id}")
async def response(user_id: int= Path(ge=1,le=100,description='Enter User ID', example='31')) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user/{username}/{age}")
async def id_response(username: str = Path(min_length=5,max_length=20,description='Enter username', example='Eugene'),
        age: int = Path(ge=18,le=120,description='Enter age', example='52')) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
