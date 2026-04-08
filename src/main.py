from aluguel import adicionar_inquilino, listar_inquilinos

while True:
    print("\n1 - Adicionar Inquilino")
    print("2 - Listar Inquilinos")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        valor = float(input("Valor: "))
        adicionar_inquilino(nome, valor)

    elif op == "2":
        listar_inquilinos()

    elif op == "0":
        break
