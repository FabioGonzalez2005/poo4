import pytest
from practicarParaExamen2 import ManejadorListas

def test_obtenerPares():
    listaPrueba = [1, 2, 3, 4, 5, 6, 7, 8]
    manejador = ManejadorListas(listaPrueba)
    assert manejador.obtenerPares() == [2, 4, 6, 8]

    listaPrueba2 = [11, 12, 13, 14, 15, 16, 17, 18]
    manejador = ManejadorListas(listaPrueba2)
    assert manejador.obtenerPares() == [12, 14, 16, 18]

    assert 