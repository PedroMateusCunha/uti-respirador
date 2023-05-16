from respirador import Respirador
import pytest
import sys
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)


def test_respirador_inicializado_corretamente():
    respirador = Respirador()
    assert respirador.irpm == 12
    assert respirador.volume_corrente == 500
    assert respirador.ligado == False


def test_set_irpm():
    respirador = Respirador()
    respirador.set_irpm(15)
    assert respirador.irpm == 15


def test_set_volume_corrente():
    respirador = Respirador()
    respirador.set_volume_corrente(600)
    assert respirador.volume_corrente == 600


def test_get_quantidade_irpm():
    respirador = Respirador()
    respirador.set_irpm(15)
    assert respirador.get_quantidade("irpm") == 15


def test_get_quantidade_volume_corrente():
    respirador = Respirador()
    respirador.set_volume_corrente(600)
    assert respirador.get_quantidade("volume_corrente") == 600


def test_ligar():
    respirador = Respirador()
    respirador.ligar()
    assert respirador.ligado == True


def test_desligar():
    respirador = Respirador()
    respirador.desligar()
    assert respirador.ligado == False


def test_get_status():
    respirador = Respirador()
    status = respirador.get_status()
    assert status == {
        "respirador": {
            "irpm": 12,
            "volume_corrente": 500,
            "ligado": False
        }
    }
