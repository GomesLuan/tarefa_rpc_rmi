import psutil
import Pyro5.api


# definindo a classe com os objetos remotos via decorators
@Pyro5.api.expose
class Monitor(object):
    # obtendo o valor da CPU
    def CPU(self):
        return psutil.cpu_percent(interval=1)

    # obtendo a memoria
    def Memoria(self):
        return psutil.virtual_memory().percent
    
    def Disk(self):
        return psutil.disk_usage('/')
    
    def Pids(self):
        return len(psutil.pids())
    
# utilizar este campo quando rodar na nuvem
# IPNUVEM = "a.b.c.d"
PORTA = 8080
PORTA_NS = 8888

# criando um serviço Pyro
#daemon = Pyro5.server.Daemon()
daemon = Pyro5.server.Daemon(host="0.0.0.0", port=PORTA)
#daemon = Pyro5.server.Daemon(host="0.0.0.0", port=8080, nathost=IPNUVEM)

# NOTE: https://psutil.readthedocs.io/en/latest/

# NOTE: precisa executar o name server em alguma porta,
# antes de executar o servidor:
# pyro5-ns -n 0.0.0.0 -p 8888

# encontrando um name server
ns = Pyro5.api.locate_ns(port=PORTA_NS)

# registrando a classe como um objeto Pyro
uri = daemon.register(Monitor)

print(uri)

# registrando o objeto com um nome no name server
ns.register("monitor", uri)

print("Pronto.")

# iniciando o loop do servidor para aguradar chamadas
daemon.requestLoop()