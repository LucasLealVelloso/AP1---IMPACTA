from pydantic import BaseModel

class ProdutosSchema(BaseModel):
    id: int
    item: str
    peso: float
    numero_caixas: int


class UsersSchema(BaseModel):
    id: int
    username: str
    password: str
    data_nasc: str
    cpf: str
    email: str