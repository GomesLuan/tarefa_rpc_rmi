import sys
import xmlrpc.client

if len(sys.argv) != 3:
    print("Erro: informe o nome e mensagem")
    print(f"{sys.argv[0]} nome mensagem")
    exit(1)

# dados da conexao com o servidor
IP = "3.87.17.216"
PORTA = 80

# obtendo o login do usuario
nome = sys.argv[1]
msg = sys.argv[2]

# conectando ao servidor
s = xmlrpc.client.ServerProxy(f"http://{IP}:{PORTA}/")

# formato do chat:
# [
#     (nome1: msg1),
#     (nome2: msg2),
#     ...
# ]

# enviando uma mensagem
s.falar(nome, msg)

# obtendo as mensagens que estao no chat
for msg in s.mensagens():
    print(f"{msg[0]}: {msg[1]}")
