from typing import Union

from fastapi import FastAPI

from model.Pokemon import Pokemon

app = FastAPI()

pokemones = {}

def crearPokemon(id, name, types, stats):
    pokemon=Pokemon(1, name, types, stats)
    pokemones[pokemon.id] = pokemon

crearPokemon("bulbasaur", 1,  ["planta", "veneno"], [ {"name": "hp","base_stat": 45},{"name":"attack","base_stat": 49},{"name": "defense","base_stat": 49},{"name": "special-attack","base_stat": 65}, {"name": "special-defense","base_stat": 65}, {"name": "speed", "base_stat": 45}], )

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/elrio")
def read_root():
    return {"El rio": "una mierda https://www.youtube.com/watch?v=-ApUNLzsSRc"}


@app.get("/getpokemon/{item_id}")
def read_itemread_item(item_id: int):
    try:
        text = pokemones[item_id]
    except KeyError:
        return {"ERROR: ": 404}

    return {text}

@app.post("/createpokemon/{name}")
def read_itemread_item(name):
    if not (name.isdigit()):
        try:
            pokeTemp = Pokemon(name)
            pokemones[name]=pokeTemp
            text = name + " created"
            return {"return": text}
        except KeyError:
            return {"ERROR: ": 404}
    else:
        text = "No valido"
    return {"return": text}