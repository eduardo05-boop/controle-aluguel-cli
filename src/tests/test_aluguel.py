from src.aluguel import adicionar_inquilino, carregar

def test_add():
    adicionar_inquilino("Teste", 500)
    dados = carregar()
    assert any(d["nome"] == "Teste" for d in dados)

def test_valor_negativo():
    try:
        adicionar_inquilino("Erro", -10)
        assert False
    except:
        assert True
