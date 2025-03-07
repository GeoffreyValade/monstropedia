from typing import Union, List, Optional
from fastapi import FastAPI, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

with open("monsters.json", "r") as f:
    monsters_list = json.load(f)

list_monsters = {k+1:v for k, v in enumerate(monsters_list)}

class Monster(BaseModel): # utilisation de BaseModel pour validation API via Pydantic
    id: int
    name: str
    types: str
    cr: Union[str, int]
    alignment: str
    ac: int
    hp: int
    height: str
    speed: str
    legendary: bool

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/total_monsters")
def get_total_monsters() -> dict:
    return {"total":len(list_monsters)}

@app.get("/monsters")
def get_all_monsters(
    name: Optional[str] = None,
    types: Optional[str] = None,
    alignment: Optional[str] = None
) -> List[Monster]:
    filtered_monsters = list_monsters.values()

    if name:
        filtered_monsters = [monster for monster in filtered_monsters if name.lower() in monster['name'].lower()]

    if types:
        filtered_monsters = [monster for monster in filtered_monsters if types.lower() in monster['types'].lower()]

    if alignment:
        filtered_monsters = [monster for monster in filtered_monsters if alignment.lower() in monster['alignment'].lower()]

    return [Monster(**monster) for monster in filtered_monsters]



@app.get("/monster/{id}")
def get_monster_by_id(id: int = Path(ge=1)) -> Monster:
    if id not in list_monsters :
        raise HTTPException(status_code=404, detail="Ce monstre n'existe pas")
    
    return Monster(**list_monsters[id])


@app.post("/monster/")
def create_monster(monster:Monster) -> Monster :
    if monster.id in list_monsters :
        raise HTTPException(status_code=404, detail=f"Le monstre {monster.id} existe déjà")
    
    list_monsters[monster.id] = monster.model_dump()
    return monster


@app.put("/monster/{id}")
def update_monster(monster: Monster, id: int = Path(ge=1)) -> Monster :
    if id not in list_monsters :
        raise HTTPException(status_code=404, detail="Ce monstre n'existe pas")
    
    list_monsters[id] = monster.model_dump()
    return monster


@app.delete("/monster/{id}")
def delete_monster(id: int = Path(ge=1)) -> Monster :
    if id in list_monsters :
        monster = Monster(**list_monsters[id])
        del list_monsters[id]
        return monster
    
    raise HTTPException(status_code=404, detail="Ce monstre n'existe pas")

@app.get("/types")
def get_all_types() -> List[str]:
    types = set()                   # utilisation du set pour éviter les doublons
    for monster in monsters_list:   # pour chaque monstre dans ma liste de monstres :
        types.add(monster["types"]) # j'ajoute son type dans ma liste types
    
    sorted_types = sorted(types)    # je trie ma liste de types
    return sorted_types             # je renvoie la liste


@app.get("/alignments")
def get_all_alignments() -> List[str]:
    alignments = set()
    for monster in monsters_list:
        alignments.add(monster["alignment"])
    
    sorted_alignments = sorted(alignments)
    return sorted_alignments

