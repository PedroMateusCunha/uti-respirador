class Respirador:
    def __init__(self):
        self.irpm = 12
        self.volume_corrente = 500
        self.ligado = False

    def set_irpm(self, irpm: int):
        self.irpm = irpm

    def set_volume_corrente(self, volume_corrente: int):
        self.volume_corrente = volume_corrente

    def get_quantidade(self, item):
        return getattr(self, f"qtd_{item}")

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def get_status(self):
        return { "respirador": {
            "irpm": self.irpm,
            "volume_corrente": self.volume_corrente,
            "ligado": self.ligado
        }
    }