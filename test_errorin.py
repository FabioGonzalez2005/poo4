import pytest
from errorin import Errorin

@pytest.fixture
def prueba1():
    assert Errorin(lista = [1, 2, 3, 4, 5, 6]) == None
    assert Errorin(lista2 = [1, 2, 3]) == IndexError
