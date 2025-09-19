from xmlrpc.server import SimpleXMLRPCServer

chat = []

# função falar
def falar(nome, msg):
    chat.append((nome, msg))

# função mensagens
def mensagens():
    return chat

# dados de conexão com o servidor
IP = ""
PORTA = 80

# criando servidor RPC
server = SimpleXMLRPCServer((IP, PORTA), allow_none=True)

# registrando as funções que serão ofertadas
server.register_function(falar, 'falar')
server.register_function(mensagens, 'mensagens')

# rodando o main loop do servidor
server.serve_forever()