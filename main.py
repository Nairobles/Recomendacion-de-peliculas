from fastapi import FastAPI
import requests
import funciones as f

app = FastAPI(title="Proyecto Individual 1",
              description="Consultas de peliculas",
              version="1.0.1"
)

#------------------------------------
# http://localhost:8000/filmaciones_mes?mes=Enero
@app.get("/filmaciones_mes")

async def filmaciones_mes(mes:str):
    respuesta = f.cantidad_filmaciones_mes(mes)
    return respuesta
#------------------------------------
# http://localhost:8000/filmaciones_dia?dia=Sabado
@app.get("/filmaciones_dia")

async def filmaciones_dia(dia:str):
    respuesta = f.cantidad_filmaciones_dia(dia)
    return respuesta
#------------------------------------
# http://localhost:8000/score_titulo?titulo=Forrest Gump
@app.get("/score_titulo")

async def score_titulo(titulo:str):
    respuesta = f.score_titulo(titulo)
    return respuesta
#------------------------------------
# http://localhost:8000/votos_titulo?titulo=Toy Story
@app.get("/votos_titulo")

async def votos_titulo(titulo:str):
    respuesta = f.votos_titulo(titulo)
    return respuesta
#-------------------------------------
# http://localhost:8000/actor?actor=Tom Hanks
@app.get("/actor")

async def get_actor(actor:str):
    respuesta = f.get_actor(actor)
    return respuesta
#--------------------------------------
# http://localhost:8000/director?director=Christopher Nolan
@app.get("/director")

async def get_director(director:str):
    respuesta = f.get_director(director)
    return respuesta

#--------------------------------------
# http://localhost:8000/recomendacion?titulo=Iron Man
@app.get("/recomendacion")

async def recomendacion(titulo:str):
    respuesta = f.recomendacion(titulo)
    return respuesta

#Cambia el puerto para que corra en Render
if __name__== "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
