from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Texto(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

@app.post("/sentimento")
def sentimento(dado: Texto):
    texto = dado.texto.lower()

    if "bom" in texto:
        resultado = "positivo"
    elif "ruim" in texto:
        resultado = "negativo"
    else:
        resultado = "neutro"

    return {"texto": dado.texto, "sentimento": resultado}