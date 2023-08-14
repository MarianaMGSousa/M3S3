import pytest
from exercicio3 import (
    calcular_preco_volume,
    validar_medida,
    calcular_multiplicador_peso,
    calcular_multiplicador_rota,
    calcular_frete
)

# Testes para a função calcular_preco_volume
def test_calcular_preco_volume():
    assert calcular_preco_volume(500) == 10.0
    assert calcular_preco_volume(5000) == 20.0
    assert calcular_preco_volume(15000) == 30.0
    assert calcular_preco_volume(50000) == 20.0

# Testes para a função validar_medida
def test_validar_medida():
    assert validar_medida("10") == 10
    assert validar_medida("abc") == -1

# Testes para a função calcular_multiplicador_peso
def test_calcular_multiplicador_peso():
    assert calcular_multiplicador_peso(0.05) == 1.0
    assert calcular_multiplicador_peso(0.5) == 1.5
    assert calcular_multiplicador_peso(5) == 2.0
    assert calcular_multiplicador_peso(20) == 3.0

# Testes para a função calcular_multiplicador_rota
def test_calcular_multiplicador_rota():
    assert calcular_multiplicador_rota("rs") == 1.0
    assert calcular_multiplicador_rota("SB") == 1.2
    assert calcular_multiplicador_rota("br") == 1.5

# Testes para a função calcular_frete
def test_calcular_frete():
    assert calcular_frete(100, 2.0, 1.5) == 300.0
    assert calcular_frete(500, 1.5, 1.2) == 900.0