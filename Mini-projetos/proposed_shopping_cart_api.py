from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()

OK = "OK"
FAILED = "FAILED"


# Class for client address data
class Address(BaseModel):
    street: str
    zipcode: str
    city: str
    state: str


# Class for client data
class Usuario(BaseModel):
    id: int
    name: str
    email: str
    password: str


# Classe representando a lista de endereços de um cliente
class ListaDeAddresssDoUsuario(BaseModel):
    usuario: Usuario
    Addresss: List[Address] = []


# Classe representando os dados do produto
class Produto(BaseModel):
    id: int
    name: str
    descricao: str
    preco: float


# Classe representando o carrinho de compras de um cliente com uma lista de produtos
class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    id_produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int


db_usuarios = {}
db_produtos = {}
db_end = {}        # Addresss_dos_usuarios
db_carrinhos = {}


# Criar um usuário,
# se tiver outro usuário com o mesmo ID retornar FAILED, 
# se o email não tiver o @ retornar FAILED, 
# password tem que ser maior ou igual a 3 caracteres, 
# senão retornar OK
@app.post("/usuario/")
async def criar_usuário(usuario: Usuario):
    if usuario.id in db_usuarios:
        return FAILED
    db_usuarios[usuario.id] = usuario
    return OK


# Se o id do usuário existir, retornar os dados do usuário
# senão retornar FAILED
@app.get("/usuario/")
async def retornar_usuario(id: int):
    if id in db_usuarios:
        return db_usuarios[id]
    return FAILED


# Se existir um usuário com exatamente o mesmo name, retornar os dados do usuário
# senão retornar FAILED
@app.get("/usuario/name")
async def retornar_usuario_com_nome(name: str):
    return FAILED


# Se o id do usuário existir, deletar o usuário e retornar OK
# senão retornar FAILED
# ao deletar o usuário, deletar também endereços e carrinhos vinculados a ele
@app.delete("/usuario/")
async def deletar_usuario(id: int):
    return FAILED


# Se não existir usuário com o id_usuario retornar FAILED, 
# senão retornar uma lista de todos os endereços vinculados ao usuário
# caso o usuário não possua nenhum endereço vinculado a ele, retornar 
# uma lista vazia
### Estudar sobre Path Params (https://fastapi.tiangolo.com/tutorial/path-params/)
@app.get("/usuario/{id_usuario}/endereços/")
async def retornar_Addresss_do_usuario(id_usuario: int):
    return FAILED


# Retornar todos os emails que possuem o mesmo domínio
# (domínio do email é tudo que vêm depois do @)
# senão retornar FAILED
@app.get("/usuarios/emails/")
async def retornar_emails(dominio: str):
    return FAILED


# Se não existir usuário com o id_usuario retornar FAILED, 
# senão cria um endereço, vincula ao usuário e retornar OK
@app.post("/Address/{id_usuario}/")
async def criar_Address(Address: Address, id_usuario: int):
    return OK


# Se não existir endereço com o id_Address retornar FAILED, 
# senão deleta endereço correspondente ao id_Address e retornar OK
# (lembrar de desvincular o endereço ao usuário)
@app.delete("/Address/{id_Address}/")
async def deletar_Address(id_Address: int):
    return OK


# Se tiver outro produto com o mesmo ID retornar FAILED, 
# senão cria um produto e retornar OK
@app.post("/produto/")
async def criar_produto(produto: Produto):
    return OK


# Se não existir produto com o id_produto retornar FAILED, 
# senão deleta produto correspondente ao id_produto e retornar OK
# (lembrar de desvincular o produto dos carrinhos do usuário)
@app.delete("/produto/{id_produto}/")
async def deletar_produto(id_produto: int):
    return OK


# Se não existir usuário com o id_usuario ou id_produto retornar FAILED, 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
@app.post("/carrinho/{id_usuario}/{id_produto}/")
async def adicionar_carrinho(id_usuario: int, id_produto: int):
    return OK


# Se não existir carrinho com o id_usuario retornar FAILED, 
# senão retorna o carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_carrinho(id_usuario: int):
    return CarrinhoDeCompras


# Se não existir carrinho com o id_usuario retornar FAILED, 
# senão retorna o o número de itens e o valor total do carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_total_carrinho(id_usuario: int):
    numero_itens, valor_total = 0
    return numero_itens, valor_total


# Se não existir usuário com o id_usuario retornar FAILED, 
# senão deleta o carrinho correspondente ao id_usuario e retornar OK
@app.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    return OK


@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')