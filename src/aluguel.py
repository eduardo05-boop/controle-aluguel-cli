import json
import os

ARQUIVO = "dados.json"

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO) as f:
        return json.load(f)

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f)

def adicionar_inquilino(nome, valor):
    if valor < 0:
        raise ValueError("Valor inválido")

    dados = carregar()
    dados.append({"nome": nome, "valor": valor})
    salvar(dados)

def listar_inquilinos():
    for d in carregar():
        print(d["nome"], "-", d["valor"])
