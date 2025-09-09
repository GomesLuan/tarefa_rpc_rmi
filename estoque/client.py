import sys
import xmlrpc.client


def help():
    print("Erro: informe a operação corretamente")
    print("adicionar produto quantidade")
    print("remover produto quantidade")
    print("consultar produto")
    print("estoque")


if len(sys.argv) < 2:
    help()
    exit(1)

# dados da conexao com o servidor
IP = "localhost"
PORTA = 8000

# conectando ao servidor
s = xmlrpc.client.ServerProxy(f"http://{IP}:{PORTA}/")

# formato do estoque:
# {
#     produto1: qtd1,
#     produto2: qtd2,
#     ...
# }

# obtendo os parametros
op = sys.argv[1]


# realizando as operacoes solicitadas
match op:

    # adicionar quantidade de produto
    case "adicionar":
        if len(sys.argv) == 4:
            produto = sys.argv[2]
            qtd = int(sys.argv[3])
            s.adicionar(produto, qtd)
        else:
            help()

    # remver quantidade de produto
    case "remover":
        if len(sys.argv) == 4:
            produto = sys.argv[2]
            qtd = int(sys.argv[3])
            s.remover(produto, qtd)
        else:
            help()

    # consulta a quantidade de itens de um produto
    case "consultar":
        if len(sys.argv) == 3:
            produto = sys.argv[2]
            print(f"{produto}: {s.consultar(produto)}")
        else:
            help()

    # retornar todo o estoque
    case "estoque":
        for produto, qtd in s.estoque().items():
            print(f"{produto}: {qtd}")

    # operacao invalida
    case _:
        print("Operacao invalida")
