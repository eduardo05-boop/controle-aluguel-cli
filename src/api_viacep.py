import requests

def consultar_cep(cep):

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    if resposta.status_code == 200:

        dados = resposta.json()

        return {
            "logradouro": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf")
        }

    return None