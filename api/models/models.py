from pydantic import BaseModel

class effectLogin(BaseModel):
    email: str
    senha: str
