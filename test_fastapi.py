from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# @app.get("/")
# def read_root():
#     return{"hello": "World"}
# Para rodar uvicorn test_fastapi:app --reload
# Para ver resultado curl http://localhost:8000



# dados = [{"1": "A"}, {"2": "B"}, {"3": "C"}]

# @app.get("/itens/")
# async def read_item(numero: int = 0):
#     return dados[numero]
# http://127.0.0.1:8000/items/?skip=0&limit=10
# https://fastapi.tiangolo.com/tutorial/query-params/


class Item(BaseModel):
    nome: str
    id: int

@app.post("/elementos/")
async def create_item(item: Item):
    return item.id, item.nome