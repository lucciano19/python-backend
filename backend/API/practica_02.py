from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#inicia el servidor: uvicorn practica_02:app --reload

#entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

#lista
users_lista = [User(id = 1, name = "lucciano", surname = "campassi", age = 17),
               User(id = 2, name = "agustina", surname = "ardiles", age = 17)]


@app.get("/users")

async def users_prueba():
    return [{"name": "lucciano", "surname": "campassi", "age": 17},
            {"name": "tiziano", "surname": "campassi", "age": 16},
            {"name": "isabella", "surname": "campassi", "age": 13},
            {"name": "agustina", "surname": "ardiles", "age": 17}]


@app.get("/usersclass/user1")

async def users():
    return users_lista


@app.get("/usersclass/user2/{id}")

async def user(id: int):
    users = filter(lambda user: user.id = id, users_lista)
    return list(users)[0]