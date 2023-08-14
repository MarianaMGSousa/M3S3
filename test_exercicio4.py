import pytest
from exercicio4 import (
    gerar_codigo,
    cadastrar_peca
)

# Antes de cada teste, podemos redefinir a lista de peças para garantir um estado limpo.
@pytest.fixture(autouse=True)
def setup():
    global pecas
    pecas = []

# Testes para a função gerar_codigo
def test_gerar_codigo_primeira_peca():
    assert gerar_codigo() == 1

def test_gerar_codigo_outras_pecas():
    pecas.append({'codigo': 1})
    assert gerar_codigo() == 1

# Testes para a função cadastrar_peca
def test_cadastrar_peca(monkeypatch):
    inputs = iter(['Nome', 'Fabricante', '10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cadastrar_peca()
    assert len(pecas) == 0