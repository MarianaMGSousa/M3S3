import pytest
from exercicio1 import exercicio1_para_teste

def test_exercicio1_menor_que_10():
    valor = exercicio1_para_teste(1, 5)
    assert valor == (5, 5)

def test_exercicio1_exatamente():
    valor = exercicio1_para_teste(1, 10)
    assert valor == (10, 9.5)

def test_exercicio1_entre_10_e_99():
    valor = exercicio1_para_teste(1, 20)
    assert valor == (20, 19)
    
def test_exercicio1_entre_100_e_999():
    valor = exercicio1_para_teste(1, 100)
    assert valor == (100, 90)
    
def test_exercicio1_maior_que_999():
    valor = exercicio1_para_teste(1, 1000)
    assert valor == (1000, 850)