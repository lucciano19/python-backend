from fastapi import FastAPI

app = FastAPI()

#metodo de fastAPI q devuelve lo q le pidamos en el parametro
@app.get("/hola mundo")

#python basico
async def hola():
    return "hola mundo con un api"

#el parametro especifica a donde lo tengo q llamar 
@app.get("/url")

async def github():
    return {"url GITHB": "https://github.com/lucciano19/python-practice"}

@app.get("/ingreso de datos")

async def nombre():
    nombre = input("nombre: ")
    edad = input("edad: ")
    return {nombre : edad}