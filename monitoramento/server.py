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

# NOTE: https://psutil.readthedocs.io/en/latest/

# NOTE: precisa executar o name server em alguma porta,
# antes de executar o servidor:
# pyro5-ns -n 0.0.0.0 -p 8888
