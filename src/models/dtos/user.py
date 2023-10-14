from pydantic import BaseModel

class UserDTO(BaseModel):
    id: int | None
    nome: str | None
    idade: int | None
    aceita_termos: bool | None