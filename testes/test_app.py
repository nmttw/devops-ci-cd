from src.app import hello

def test_hello():
    resultado = hello()
    print(\n"Resultado da função hello():", resultado)
    assert hello() == "Desafio DevOps rodando com sucesso!"
