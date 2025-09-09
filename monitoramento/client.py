import sys

import Pyro5.api

# utilizar este campo quando rodar na nuvem
IP = "127.0.0.1"
PORTA_NS = 8888

# buscando a URI do objeto remoto no name server
monit = Pyro5.api.Proxy(f"PYRONAME:monitor@{IP}:{PORTA_NS}")

print(f"CPU: {monit.CPU()}")
print(f"MEM: {monit.Memoria()} %")

# TODO: desenvolva mais duas opções de monitoramento da sua escolha
print(f"???: {monit.???()} %")
print(f"???: {monit.???()} %")
