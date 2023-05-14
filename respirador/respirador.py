"""Modulo para gerenciamento do respirador do leito hospitalar."""
class Respirador:
    """
    Classe para gerenciamento do respirador do leito hospitalar
    """
    def __init__(self):
        """
        Metodo para inicializar os atributos do respirador
        """
        self.irpm = 12
        self.volume_corrente = 500
        self.ligado = False

    def set_irpm(self, irpm: int):
        """
        Metodo para setar o valor do IRPM do respirador
        """
        self.irpm = irpm

    def set_volume_corrente(self, volume_corrente: int):
        """
        Metodo para setar o volume correte do respirador
        """
        self.volume_corrente = volume_corrente

    def get_quantidade(self, item):
        """
        Metodo para recuperar o valor setado para IRPM ou volume corrente.
        """
        return getattr(self, f"qtd_{item}")

    def ligar(self):
        """
        Metodo para ligar o respirador
        """
        self.ligado = True

    def desligar(self):
        """
        Metodo para desligar o respirador
        """
        self.ligado = False

    def get_status(self):
        """
        Metodo para recuperar o status do respirador
        """
        return { "respirador": {
            "irpm": self.irpm,
            "volume_corrente": self.volume_corrente,
            "ligado": self.ligado
        }
    }
