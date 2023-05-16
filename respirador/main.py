"""
Modulo para inicialização e disponilibilização do serviço
relacionado ao componente respirador.
"""
from fastapi import FastAPI
from respirador import Respirador

app = FastAPI()
respirador = Respirador()

@app.get("/")
def read_root():
    """Metodo para roteamento inicial do componente"""
    return {"message": "respirador"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/status")
def check_status():
    """Metodo para roteamento para checagem de status do respirador"""
    return respirador.get_status()

@app.put("/irpm/{irpm}")
def set_irpm(irpm: int):
    """Metodo para roteamento para setar valor do IRPM"""
    respirador.set_irpm(irpm)
    return {"message": "IRPM atualizado com sucesso"}

@app.put("/vc/{volume_corrente}")
def set_volume_corrente(volume_corrente: int):
    """Metodo para roteamento para setar valor do volume corrente"""
    respirador.set_volume_corrente(volume_corrente)
    return {"message": "Volume corrente atualizado com sucesso"}

@app.put("/ligar")
def ligar():
    """Metodo para roteamento para ligar o respirador."""
    respirador.ligar()
    return {"message": "respirador ligado"}

@app.put("/desligar")
def desligar():
    """Metodo para roteamento para desligar o respirador."""
    respirador.desligar()
    return {"message": "respirador desligado"}
