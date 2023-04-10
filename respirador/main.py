from fastapi import FastAPI, Request
from respirador import Respirador

app = FastAPI()
respirador = Respirador()

@app.get("/")
def read_root():
    return {"message": "respirador"}

@app.get("/status")
def check_status():
    return respirador.get_status()

@app.put("/irpm/{irpm}")
def set_irpm(irpm: int):
    respirador.set_irpm(irpm)
    return {"message": "IRPM atualizado com sucesso"}

@app.put("/vc/{volume_corrente}")
def set_volume_corrente(volume_corrente: int):
    respirador.set_volume_corrente(volume_corrente)
    return {"message": "Volume corrente atualizado com sucesso"}

@app.put("/ligar")
def ligar():
    respirador.ligar()
    return {"message": "respirador ligado"}

@app.put("/desligar")
def desligar():
    respirador.desligar()
    return {"message": "respirador desligado"}
