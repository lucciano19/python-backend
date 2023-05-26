from fastapi import FastAPI
#escribir siempre
app = FastAPI()



#metodo de fastAPI q permite leer datos en el path q especifiquemos en el parametro
@app.get("/hola")

#http://127.0.0.1:8000/hola

#python basico
async def hola():
    return "hola mundo con un api"

#el parametro especifica a donde lo tengo q llamar 
@app.get("/url")

#http://127.0.0.1:8000/url

async def github():
    return {"url GITHB": "https://github.com/lucciano19/python-practice"}


#metodo q crea datos

