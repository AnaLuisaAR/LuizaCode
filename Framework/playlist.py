import fastapi
from typing import Optional
import pydantic

songs = []

def save_song(new_song):
    codigo_new_song = len(songs) + 1
    new_song["codigo"] = codigo_new_song
    songs.append(new_song)
    return new_song

def search_music_id(id):
    res = None
    for song in songs:
        if song["codigo"] == id:
            res = song
            break 
    return res

api_rest = fastapi.FastAPI()

@api_rest.get('/')
def root_path():
    return {
        'ok': True,
        'version': 'Trial 1'
    }

class NewSong(pydantic.BaseModel):
    nome: str
    artista: str
    tempo:Optional[int]

@api_rest.post("/musicas")
def save_new_song(new_song: NewSong):
    print("Registrando uma nova musica: ", new_song.dict())
    new_song = save_song(new_song.dict())
    return new_song

@api_rest.get("/musicas")
def search_all():
    return songs

@api_rest.get("/musicas/{id}")
def search_by_id(id: int):
    print("Consulta pelo código: ", id)
    return search_music_id(id)