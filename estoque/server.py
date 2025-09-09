from xmlrpc.server import SimpleXMLRPCServer

est = {}

# função adicionar
def adicionar(produto, qtd):
    est[produto] = est.get(produto, 0) + qtd

# função remover
def remover(produto, qtd):
    est[produto] = est.get(produto, 0) - qtd
    if (est[produto] < 0):
        est[produto] = 0

# função consultar
def consultar(produto):
    est[produto] = est.get(produto, 0)
    return est[produto]

# função estoque
def estoque():
    return est

# dados de conexão com o servidor
IP = ""
PORTA = 8000

# criando servidor RPC
server = SimpleXMLRPCServer((IP, PORTA), allow_none=True)

# registrando as funções que serão ofertadas
server.register_function(adicionar, 'adicionar')
server.register_function(remover, 'remover')
server.register_function(consultar, 'consultar')
server.register_function(estoque, 'estoque')

# rodando o main loop do servidor
server.serve_forever()